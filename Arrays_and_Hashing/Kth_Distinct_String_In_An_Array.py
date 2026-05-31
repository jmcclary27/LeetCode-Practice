class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = Counter(arr)
        
        counter = 0
        for char in arr:
            if seen[char] == 1:
                counter += 1
            if counter == k:
                return char
            
        return ""