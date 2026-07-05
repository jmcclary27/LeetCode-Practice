class PrefixNode:
    def __init__(self):
        self.children = {}   # a -> PrefixNode
        self.count = 0

class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def add(self, w: str, length: int) -> None:
        cur = self.root
        for i in range(length):
            if w[i] not in cur.children:
                cur.children[w[i]] = PrefixNode()
            cur = cur.children[w[i]]
            cur.count += 1

    def count(self, pref: str) -> int:
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_tree = PrefixTree()

        for w in words:
            if len(w) >= len(pref):
                prefix_tree.add(w, len(pref))

        return prefix_tree.count(pref)