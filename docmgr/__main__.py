from mainfuncs import fetchDocList, indexDocs
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
        #Pendiente permanencia en disco

    except:
        print(f"FileNotFoundError: No such file or directory: '{path}'")
        sys.exit(0)


def search(word):
    #Recuperar estructura de disco
    #T = Trie()
    T = None
    #TODO
    print("Searching ...")
    doclist = fetchDocList(T, word)

    if doclist:
        for i in range(len(doclist)):
            if doclist[i].key == None:
                break
            print(f"({i}) {doclist[i].key}: {doclist[i].value}")
    else:
        print('no document found')



def parse_args(prog, argv):
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
    if len(os.sys.argv) > 3:
        usage(os.sys.argv[0])
        sys.exit(1)

    parse_args(os.sys.argv[0], os.sys.argv[1:])

    print(os.sys.argv)


if __name__ == "__main__":
    main()
