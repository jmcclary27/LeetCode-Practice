class WordDictionary:

    def __init__(self):
        self.wordSet = set()

    def addWord(self, word: str) -> None:
        self.wordSet.add(word)

    def search(self, word: str) -> bool:
        for w in self.wordSet:
            if re.fullmatch(word, w):
                return True
        
        return False