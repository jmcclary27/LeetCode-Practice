class PrefixTree:

    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        return True if word in self.words else False

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for pres in self.words:
            if len(pres) < n:
                continue
            if pres[:n] == prefix:
                return True
        return False