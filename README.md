# hbox

A CLI to manage packages via containers.

```sh
$ hbox 
usage: hbox [-h] {info,version,list,add,remove,run,use} ...

CLI tool to manage package versions via container images.

positional arguments:
  {info,version,list,add,remove,run,use}
                        Available commands
    info                Print debug information.
    version             Show current hbox version.
    list                List all installed packages and their versions.
    add                 Add a specific version of a package
    remove              Remove a package.
    run                 Run the package.
    use                 Set current version of a package.

options:
  -h, --help            show this help message and exit
```

## Setup

To make sure the `shims` will be added successfully, add the following line to your `.bashrc` or `.zshrc`:

```sh
export HBOX_DIR="$HOME/.hbox"
export PATH="$HBOX_DIR/shims":$PATH
```

## Features

- Uses containers to isolate packages
- Manages different versions of packages
- Customizable via configuration files
- Support pipes in `hbox run` (e.g. `echo '{"foo": 0}' | hbox run jq`)
- Adds `shims` aliases for all packages installed to avoid running `hbox run <package> <commands>`

## To do

- Support `podman`
- Support private registries and mirrors
  - maybe via registry mapping in `config.json`?
- Support local overrides for package versions
  - use merged version to allow partial overrides?
- Organize an index of packages outside this source repo
  - maybe another repo `hbox-py-index`?
- Add auto update
- Add option to keep containers instead of using `--rm`
  - maybe adding custom tags to them to identify them easily?
- Get version from git tag
- Add GitHub Actions to build and publish to PyPI
- Double check if registered packages are available locally before using them
- Add warn when a shim will conflict with an existing command
- Add `hbox config` to support all `config.json` options
- [Experimental] Identify paths in `hbox run` to map them via container volumes automatically
- Separate `packages.json` from `config.json`
  - Allow use to override `packages.json` retrieved from centralized index/repo
- Add `hbox update` to update index
- Add `hbox register` to register a package, even with custom image
- Add option to remove images when removing packages
- Allow to specify CLI name for a package (in cases a package has a name like `lambda/python`)
- Add support to colors in `hbox run` output when possible (*nix only?)
