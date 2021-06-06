import sys
import os


VERSION = "0.0.0"


def usage(prog):
    out = [
        "",
        "optional arguments:",
        "  -v, --version         show program's version number and exit",
        "  -h, --help            show this help message and exit",
        "  -c, --create PATH     create an index in the provided path",
        "  -s, --search KEYWORD  search for the provided key word in the index of the",
        "                        current directory",
    ]

    print("usage:", prog, "[OPTIONS]")
    print("\n".join(out))


def create():
    print("Indexing ...")


def search():
    print("Searching ...")


def parse_args(prog, argv):
    if (argv[0] == "-s" or argv[0] == "--search"):
        search()
    elif (argv[0] == "-c" or argv[0] == "--create"):
        create()
    elif (argv[0] == "-h" or argv[0] == "--help"):
        usage(prog)
        sys.exit(0)
    elif (argv[0] == "-v" or argv[0] == "--version"):
        print("docmgr ", VERSION)
        sys.exit(0)
    else:
        usage(prog)
        sys.exit(1)


def main():
    if len(os.sys.argv) > 3:
        usage(os.sys.argv[0])
        sys.exit(1)

    parse_args(os.sys.argv[0], os.sys.argv[1:])

    print(os.sys.argv)


if __name__ == "__main__":
    main()
