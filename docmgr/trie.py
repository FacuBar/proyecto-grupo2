from .algo1 import Array, String, concat
from .hashmap import HashMap, hashmap_insert, hashmap_search
from .linkedlist import LinkedList, Node, delete as list_delete, length, append


class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False
    # Contador de repeticiones de una palabra en cada doc
    rep = None


"""-Insert(T, element, doc): inserta element en T y contabiliza las incidencias en doc-"""


def insert(T, element, doc):
    if not T.root:
        T.root = TrieNode()
        T.root.children = LinkedList()
        T.root.children.head = Node()
        T.root.children.head.value = TrieNode()
        T.root.children.head.value.parent = T.root
        T.root.children.head.value.key = toUpp(element[0])

    return _insert(T.root.children.head.value, element, 0, doc)


def _insert(node, c, i, doc):
    # Si la key del TrieNode no coincide con el char ...
    if node.key != toUpp(c[i]):
        # Se sigue buscando en los hermanos del TrieNode ...
        cn = node.parent.children.head
        while cn:
            # Si un hno coincide, se llama la función desde este
            if cn.value.key == toUpp(c[i]):
                return _insert(cn.value, c, i, doc)

            if cn.nextNode is None:
                temp = cn
            cn = cn.nextNode
        # Si ningún hno coincide, se agrega uno que lo haga
        temp.nextNode = Node()
        temp.nextNode.value = TrieNode()
        temp.nextNode.value.parent = node.parent
        temp.nextNode.value.key = toUpp(c[i])
        return _insert(temp.nextNode.value, c, i, doc)

    else:
        if len(c) - 1 == i:
            if node.isEndOfWord is False:
                D = HashMap()
                node.rep = D
                node.isEndOfWord = True
            # Se contabiliza repeticiones de la palabra en doc

            temp = hashmap_search(node.rep, doc)
            if temp:
                temp.value += 1
            else:
                hashmap_insert(node.rep, doc)

            return node
        # Si no es final de palabra ...
        else:
            # y tiene hijos, llamada recursiva
            if node.children:
                return _insert(node.children.head.value, c, i+1, doc)
            # y no tiene hijos, se crea el TrieNode corresp y llamada recursiva
            else:
                node.children = LinkedList()
                node.children.head = Node()
                node.children.head.value = TrieNode()
                node.children.head.value.key = toUpp(c[i+1])
                node.children.head.value.parent = node
                return _insert(node.children.head.value, c, i+1, doc)


"""-Search(T, element): Devuelve el último nodo de element dentro de T-"""


def search(T, element):
    if not T.root:
        return False

    return _search(T.root.children.head.value, element, 0)


def _search(node, c, i):
    # Si la key del TrieNode no coincide con el char ...
    if node.key != toUpp(c[i]):
        # Se sigue buscando en los hermanos del TrieNode ...
        if node.parent.children is not None:
            cn = node.parent.children.head
            while cn:
                # Si un hno coincide, se llama la función desde este
                if cn.value.key == toUpp(c[i]):
                    return _search(cn.value, c, i)
                cn = cn.nextNode
            # Si el TrieNode no tiene hno, la palabra no existe
            return False

    else:
        if len(c) - 1 == i:
            if node.isEndOfWord is True:
                return node
            return False
        # Si no es final de palabra ...
        else:
            # y tiene hijos, llamada recursiva
            if node.children and length(node.children) > 0:
                return _search(node.children.head.value, c, i+1)
            # y no tiene hijos, la palabra no existe
            else:
                return False


"""-Delete(T, element): elimina element de Trie-"""


def delete(T, element):
    if not T.root:
        return False
    # Se busca el último nodo del elemento en el trie
    node = _search(T.root.children.head.value, element, 0)
    # Si el elemento no está en el nodo, return False
    if not node:
        return False

    return _delete(node)
# Se elimina desde el final del elemento hacía arriba.


def _delete(node):
    # Si el elemento está contenido dentro de otro se desmarca eow.
    if node.children and node.isEndOfWord:
        node.isEndOfWord = False
        return True

    while node.isEndOfWord is None or node.key is not None:
        # Si elemento comparte segmentos con otra palabra, se termina el proceso de eliminación
        if node.children:
            break
        # Si no lo hace, se desvincula el nodo
        list_delete(node.parent.children, node)
        node.children = None
        node = node.parent

    return True


"""-get_words(T): Devuelve una lista de todos los elementos en Trie-"""


def get_words(T):
    if not T.root or not T.root.children:
        return None
    # LD donde se almacenan palabras.
    li = LinkedList()
    _get_words(T.root, li)
    return li


def _get_words(node, li, i=0, word=Array(33, 'c')):
    if node.key is None:
        cn = node.children.head
        while cn:
            _get_words(cn.value, li)
            cn = cn.nextNode
        return

    if node.isEndOfWord is True:
        word[i] = node.key
        # caracter que denota final de palabra
        word[i + 1] = '/'
        # se crea una String con la palabra contenida en el Array
        string = get_string(word)
        append(li, string)

        if node.children:
            cn = node.children.head
            while cn:
                _get_words(cn.value, li, i + 1)
                cn = cn.nextNode

    else:
        word[i] = node.key
        cn = node.children.head
        while cn:
            _get_words(cn.value, li, i + 1)
            cn = cn.nextNode


def get_string(a):
    s = String('')
    for i in range(len_array_word(a)):
        s = concat(s, String(a[i]))
    return s

# Longitud de la palabra contenida en el array


def len_array_word(word):
    for i in range(33):
        if word[i] == '/':
            return i


def toUpp(c):
    if ord(c) > 96 and ord(c) < 123:
        return chr(ord(c) - ord('a') + ord('A'))
    else:
        return c
