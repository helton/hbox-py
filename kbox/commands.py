import os
import platform
import subprocess
from typing import Optional

import kbox.config as config
from kbox.logger import get_logger
from kbox.utils import execute_command, resolve_path

log = get_logger(__name__)


def add_shim(name: str):
    shims_file_path = resolve_path(os.path.join(config.shims_path, name))
    if not os.path.exists(shims_file_path):
        with open(shims_file_path, 'w') as shim_file:
            shim_file.write('#!/bin/sh\n')
            shim_file.write('kbox run ' + name + ' "$@"\n')

        # Set the permissions of the new shim script to be executable (0o755 gives rwx for user and rx for group/others)
        os.chmod(shims_file_path, 0o755)


def get_container_image_url(name: str, version: str):
    cfg = config.load_config()
    versions_cfg = config.load_versions()
    found = False
    for current_package in versions_cfg.packages:
        if current_package.name == name:
            if version in current_package.versions:
                log.info(f"'{name}' version {version} already exists.")
                return
            else:
                current_package.versions.append(version)
                found = True
            break
    if not found:
        package = config.Package(name=name, versions=[version], current=version)
        versions_cfg.packages.append(package)

    if name in cfg.packages:
        image = cfg.packages[name].image
    else:
        image = name

    config.save_versions(versions_cfg)

    return f"{image}:{version}"


def add_package(name, version="latest"):
    image_url = get_container_image_url(name, version)
    if image_url:
        full_command = ["docker", "pull", image_url]
        log.debug(f"Running command: {' '.join(full_command)}")
        try:
            execute_command(full_command)
        except subprocess.CalledProcessError as e:
            log.error(f"Failed to add '{name}' version {version}.")
        else:
            log.info(f"Added '{name}' version {version}.")
            add_shim(name)


def run_package(name: str, command: list):
    cfg = config.load_config()
    versions_cfg = config.load_versions()

    image = name
    version = "latest"

    volumes_command = []
    if name in cfg.packages:
        package = cfg.packages[name]
        image = package.image
        for current_package in versions_cfg.packages:
            if current_package.name == name:
                version = current_package.current
        for volume in package.volumes:
            source = resolve_path(volume.source)
            target = volume.target
            if os.path.exists(source):
                log.debug(f"Mounting volume {source} to {target}")
                volumes_command.extend(["-v", f"{source}:{target}"])
            else:
                log.debug(f"Volume {source} not found. Skipping.")
    else:
        log.debug(f"No configuration found for package '{name}'. Using {name} as the image name.")

    full_image_url = f"{image}:{version}"
    full_command = ["docker", "run", "--rm", full_image_url] + volumes_command + command

    log.debug(f"Running command: {' '.join(full_command)}")
    execute_command(full_command)


def set_package_version(name: str, version: str):
    versions_cfg = config.load_versions()
    for current_package in versions_cfg.packages:
        if current_package.name == name:
            if version in current_package.versions:
                current_package.current = version
                config.save_versions(versions_cfg)
                log.info(f"'{name}' set to version {version}")
            else:
                log.error(f"'{name}' version {version} not found. Add the version first via 'add' command.")


def show_info():
    log.info("OS:")
    os_info = ' '.join(platform.uname())
    log.info(os_info)

    log.info("\nKBOX VERSION:")
    log.info(config.version)

    log.info("\nKBOX ENVIRONMENT VARIABLES:")
    log.info(f"KBOX_DIR={config.base_dir}")


def show_version():
    log.info(config.version)


def print_package(package):
    sorted_versions = sorted(package.versions)
    for version in sorted_versions:
        msg = f"- {package.name}@{version}"
        if version == package.current:
            msg += " (current)"
        log.info(msg)


def list_packages(name: Optional[str] = None):
    versions_cfg = config.load_versions()
    if name:
        found = False
        for package in versions_cfg.packages:
            if package.name == name:
                print_package(package)
                found = True
                break
        if not found:
            log.error(f"Package '{name}' was not found. Add the package first via 'add' command.")
    else:
        for package in sorted(versions_cfg.packages, key=lambda pkg: pkg.name):
            print_package(package)
