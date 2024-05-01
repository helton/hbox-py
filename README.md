# kbox

A CLI to manage packages via containers.

```sh
$ kbox
usage: kbox [-h] {info,version,list,add,run,use} ...

CLI tool to manage package versions via container images.

positional arguments:
  {info,version,list,add,run,use}
                        Available commands
    info                Print debug information.
    version             Show current version.
    list                List all installed packages and their versions.
    add                 Add a specific version of a package
    run                 Run the package.
    use                 Set current version of a package.

options:
  -h, --help            show this help message and exit
```

## Setup

To make sure the `shims` will be added successfully, add the following line to your `.bashrc` or `.zshrc`:

```sh
export KBOX_DIR="$HOME/.kbox"
export PATH="$KBOX_DIR/shims":$PATH
```

## Features

- Uses containers to isolate packages
- Manages different versions of packages
- Customizable via configuration files
- Support pipes in `kbox run` (e.g. `echo '{"foo": 0}' | kbox run jq`)
- Adds `shims` aliases for all packages installed to avoid running `kbox run <package> <commands>`

## To do

- Support `podman`
- Support private registries and mirrors
  - maybe via registry mapping in `config.json`?
- Support local overrides for package versions
  - use merged version to allow partial overrides?
- Organize an index of packages outside this source repo
  - maybe another repo `kbox-py-index`?
- Add auto update
- Add option to keep containers instead of using `--rm`
  - maybe adding custom tags to them to identify them easily?
- Get version from git tag
- Add GitHub Actions to build and publish to PyPI
- Double check if registered packages are available locally before using them
- Add warn when a shim will conflict with an existing command
- Add `kbox remove` command
- Add `kbox config` to support all `config.json` options
- [Experimental] Identify paths in `kbox run` to map them via container volumes automatically
- Separate `packages.json` from `config.json`
  - Allow use to override `packages.json` retrieved from centralized index/repo
- Add `kbox update` to update index
- Add `kbox register` to register a package, even with custom image
