# Roadmap

List of ideas I want to implement in the future.

- Miscellaneous:
  - Rewrite in Rust 🦀
  - Support `podman`
  - Support private registries and mirrors
    - maybe via registry mapping in `config.json`?
  - Support local overrides for package versions
    - use merged version to allow partial overrides?
  - Create an index/registry repository
    - Use shards to get better performance in git repositories
      - References:
        - https://github.com/Homebrew/homebrew-core
        - https://github.com/Homebrew/homebrew-cask
        - https://github.com/opentofu/opentofu/issues/741#issuecomment-1777544250
    - Double check if registered packages are available locally before using them
    - Separate `index.json` from `config.json`
      - Allow use to override `index.json` retrieved from centralized index/repo
- New commands
  - Add auto update `hbox upgrade`
  - Add `hbox update` to update index
  - Add `hbox register` to register a package, even with custom image
  - Add `hbox verify` to check if there's something wrong with packages or with container engine:
    - Verify if `docker` or `podman` are installed and available
      - Verify if there are container images for the current version of each package
  - Add command `hbox reshim` to regenerate shims
  - *Experimental*: Identify paths in `hbox run` to map them via container volumes automatically
- Updated commands:
  - Allow `hbox config` to support all `config.json` options
  - Add option to keep containers instead of using `--rm`
    - maybe adding custom tags to them to identify them easily?
  - Add option to remove images when removing packages via `hbox remove/uninstall`
  - Add support to colors in `hbox run` output when possible (*nix only?)
  - On `hbox add/install` add warn when a shim will conflict with an existing command
- Technical debt:
  - Add unit and integration tests
    - it should run on Linux and Windows 
