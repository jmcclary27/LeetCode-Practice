class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Creates our two outer indexes
        low, high = 0, len(nums) - 1

        # Loops until low is greater than high (target is not in array)
        while low <= high:
            # Calculates our middle index
            mid = (high + low) // 2
            # Checks if the number at the middle index is our target
            if nums[mid] == target:
                return mid
            # Checks if the number at the middle index is less than our target
            elif nums[mid] < target:
                low = mid + 1
            # Checks if the number at the middle index is greater than our target
            else:
                high = mid - 1
        # Returns -1 if number is not in array
        return -1