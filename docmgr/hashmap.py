from math import floor

from .algo1 import Array


SIZE = 1000
A = 1.61803398874989484820


class HashMap:
    head = None


class HashMapNode:
    value = None
    key = None
    seqHeight = 0


def key_hash(k):
    b = str.encode(k)
    h = 0

    for c in range(0, len(b)):
        h += floor(SIZE * (b[c]*A % 1))

    return h % SIZE


def hashmap_insert(D, k, v = 1):
    i = key_hash(k)

    if not D.head:
        D.head = Array(SIZE, HashMapNode())

    n = _new_hash_node(k, v)
    cur = D.head[i]
    if cur is None:
        D.head[i] = n
    else:
        seqHeight = 0
        h = i

        while cur is not None:
            if (seqHeight > cur.seqHeight):
                n.seqHeight = seqHeight
                seqHeight = cur.seqHeight

                temp = cur
                D.head[i] = n
                n = temp

            seqHeight += 1

            i += 1
            if i >= SIZE:
                i -= SIZE
            if i == h:
                raise MemoryError("ERROR! Full hashmap.")

            cur = D.head[i]

        n.seqHeight = seqHeight
        D.head[i] = n


def _search(D, i, k):
    if D.head is None:
        return None

    if D.head[i] is None:
        return None

    h = i
    while D.head[i] is not None:
        if D.head[i].key == k:
            return D.head[i]

        i += 1

        if i == h:
            return None
        if i >= SIZE:
            i -= SIZE

    return None


def hashmap_search(D, k):
    i = key_hash(k)

    return _search(D, i, k)


def delete(D, k):
    h = key_hash(k)

    i = _search(D, h, k)
    if i < 0:
        return None

    pre = D.head[i]
    D.head[i] = None
    ret = pre

    j = i + 1
    if j >= SIZE:
        j -= SIZE
    cur = D.head[j]

    while pre is not None:
        D.head[i] = cur
        D.head[i].seqHeight -= 1
        pre = cur

        i = j
        j += 1
        if j >= SIZE:
            j -= SIZE

        temp = D.head[j]
        cur = temp

        if cur is None or cur.seqHeight == 0:
            break

        D.head[j] = None

    return ret


def _new_hash_node(k, v):
    n = HashMapNode()
    n.key = k
    n.value = v

    return n


def print_hashmap(D):
    for i in range(0, SIZE):
        if D.head[i] is not None:
            print(D.head[i].key)
            print(" ", D.head[i].value, D.head[i].seqHeight, i)


#    print(key_hash("hello"))
#    print(key_hash("cuu"))
#    D = HashMap()
#    hashmap_insert(D, "hello", 5)
#    hashmap_insert(D, "cuu\\", 6)
#    hashmap_insert(D, "bye", 8)
#    hashmap_insert(D, "test", 12)
#    hashmap_insert(D, "good", 3)
#    hashmap_insert(D, "good", 3)
#    hashmap_insert(D, "cuu\\", 6)
#    hashmap_insert(D, "good", 3)
#    hashmap_insert(D, "cuu\\", 6)
#    hashmap_insert(D, "good", 3)
#    hashmap_insert(D, "cuu\\", 6)
#    hashmap_insert(D, "cuu%", 7)
#    print_hashmap(D)
#
#    print()
#    print("Deletion")
#    delete(D, "cuu\\")
#    print_hashmap(D)
