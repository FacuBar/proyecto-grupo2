import json

from .hashmap import HashMap, hashmap_insert
from .trie import Trie, insert as trie_insert


class Occurrence:
    line = -1
    column = -1


class LinkedListIter:
    def __init__(self, head):
        self.cur = head

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration

        ret = self.cur
        self.cur = self.cur.nextNode

        return ret


class DocMgrJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Trie):
            return list(LinkedListIter(obj.head))
        elif isinstance(obj, HashMap):
            dct = {}
            return dct
        elif isinstance(obj, Occurrence):
            dct = {}
            dct["@line"] = obj.line
            dct["@column"] = obj.column
            return dct

        return None


def entry_pairs_hook(pair_list):
    entry_map = None
    trie = None
    occur = Occurrence()

    print(pair_list)

    for i, (k, v) in enumerate(pair_list):
        if type(v) is Occurrence:
            if entry_map is None:
                entry_map = HashMap()

            hashmap_insert(entry_map, k, v)

            continue

        elif type(v) is HashMap:
            if trie is None:
                trie = Trie()

            trie_insert(trie, k, v)

        if k == "@line":
            occur.line = v
        elif k == "@column":
            occur.column = v

        if occur.line > -1 and occur.column > -1:
            return occur

    if entry_map is not None:
        return entry_map

    if trie is not None:
        return trie

    return None


def load_json(jf):
    return json.load(jf, object_pairs_hook=entry_pairs_hook)


def loads_json(jd):
    return json.loads(jd, object_pairs_hook=entry_pairs_hook)


def dump_json(jf):
    return json.dump(jf, cls=DocMgrJSONEncoder)


def dumps_json(jd):
    return json.dumps(jd, cls=DocMgrJSONEncoder)
