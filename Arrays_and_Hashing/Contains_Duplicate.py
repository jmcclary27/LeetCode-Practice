class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Returns True if there are duplicates in the list, False otherwise.
        return len(set(nums)) < len(nums)