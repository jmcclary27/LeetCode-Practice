class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creates dictionary keeping track of the occurences of each number
        count = {}
        # Creates a list of lists where the index represents the frequency
        # and the elements at that index are the numbers with that frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Loops through the numbers and fills the count dictionary and the freq list
        for num in nums:
            count[num] = 1 + count.get(nums, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Collects the top k frequent elements
        res = []
        # Iterate from the end of freq to the beginning to get the most frequent elements first
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res