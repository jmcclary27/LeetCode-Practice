class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first1, back1, first2, back2 = 0, 0, 0, 0
        while first1 < len(word1) and first2 < len(word2):
            if word1[first1][back1] == word2[first2][back2]:
                if back1 == len(word1[first1]) - 1:
                    back1 = 0
                    first1 += 1
                else:
                    back1 += 1
                
                if back2 == len(word2[first2]) - 1:
                    back2 = 0
                    first2 += 1
                else: 
                    back2 += 1
            else:
                return False
        
        return False if first1 < len(word1) or first2 < len(word2) else True