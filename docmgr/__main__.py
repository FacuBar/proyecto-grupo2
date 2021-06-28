from .mainfuncs import fetchDocList, indexDocs
from .serializacion import load
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


def create(path):
    if path[-1:] != '/':
        path += '/'

    try:
        docs = os.listdir(path)
        print("Indexing ...")
        indexDocs(path, docs)
        print('library created successfully')

        sys.exit(0)

    except Exception as e:
        print("Index could not be created:", file=sys.stderr)
        print(e.__class__.__name__ + ":", e, file=sys.stderr)
        sys.exit(1)


def search(word):
    print("Searching ...")

    try:
        T = load()
    except Exception as e:
        print("No document found:", file=sys.stderr)
        print(e.__class__.__name__ + ":", e, file=sys.stderr)
        sys.exit(1)

    doclist = fetchDocList(T, word)

    if doclist:
        for i in range(len(doclist)):
            if doclist[i].key is None:
                break
            print(f"({i+1}) {doclist[i].key}: {doclist[i].value}")
    else:
        print('no document found')

    sys.exit(0)


def parse_args(prog, argv):
    if len(argv) > 2:
        usage(prog)
        sys.exit(1)

    if (argv[0] == "-s" or argv[0] == "--search"):
        search(argv[1])
    elif (argv[0] == "-c" or argv[0] == "--create"):
        create(argv[1])
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
    parse_args(os.sys.argv[0], os.sys.argv[1:])


if __name__ == "__main__":
    main()
