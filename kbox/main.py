import argparse

from kbox.commands import show_info, show_version, add_package, run_package, set_package_version, \
    list_packages, remove_package


def run():
    parser = argparse.ArgumentParser(description="CLI tool to manage package versions via container images.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("info", help="Print debug information.")

    subparsers.add_parser("version", help="Show current kbox version.")

    parser_list = subparsers.add_parser("list", help="List all installed packages and their versions.")
    parser_list.add_argument("name", type=str, nargs='?', default=None, help="Show all versions for a given package.")

    parser_add = subparsers.add_parser("add", help="Add a specific version of a package")
    parser_add.add_argument("name", type=str, help="Name of the package to install")
    parser_add.add_argument("version", nargs="?", type=str, default="latest",
                            help="Version of the package (default: latest)")
    parser_add.add_argument("-d", "--set-default", action="store_true",
                            help="Set the added version as the current version")

    parser_remove = subparsers.add_parser('remove', help='Remove a package.')
    parser_remove.add_argument('name', help='The name of the package to remove.')
    parser_remove.add_argument("version", nargs="?", type=str, default=None,
                               help="Version of the package (default: latest)")

    parser_run = subparsers.add_parser("run", help="Run the package.")
    parser_run.add_argument("name", type=str, help="Name of the package to run")
    parser_run.add_argument("subcommand", nargs=argparse.REMAINDER, help="Arguments to pass to the package")

    parser_set = subparsers.add_parser("use", help="Set current version of a package.")
    parser_set.add_argument("name", type=str, help="Name of the package to set the version of.")
    parser_set.add_argument("version", type=str, help="New version to set as current.")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    elif args.command == "info":
        show_info()
    elif args.command == "version":
        show_version()
    elif args.command == "list":
        list_packages(args.name)
    elif args.command == "add":
        add_package(args.name, args.version, args.set_default)
    elif args.command == "remove":
        remove_package(args.name, args.version)
    elif args.command == "use":
        set_package_version(args.name, args.version)
    elif args.command == "run":
        run_package(args.name, args.subcommand)


if __name__ == "__main__":
    run()
