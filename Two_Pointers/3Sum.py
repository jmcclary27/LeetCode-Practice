class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Creates final array to store all the 3 sums
        res = []
        # Sorts numbers into nondecreasing order (O(nlogn))
        nums.sort()

        # Loops through nums (i is the index and a is the number)
        for i, a in enumerate(nums):
            # Checks if our first pointer is in the positives and breaks if true
            # This happens because our array is sorted, so if a is positive, so are the other two pointers, making it impossible to add to 0
            if a > 0:
                break
            
            # Checks for duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            # Establishes our other two pointers at one after a, and at the end
            l, r = i + 1, len(nums) - 1
            # Loops until l and r meet
            while l < r:
                # Computes the sum of the three numbers
                threeSum = a + nums[l] + nums[r]
                # Checks if threeSum is greater than zero, and if it is, we decrement r (trying to shrink our sum)
                if threeSum > 0:
                    r -= 1
                # Checks if threeSum is less than zero, and if it is, we increment l (trying to grow our sum)
                elif threeSum < 0:
                    l += 1
                # Executes if our sum is 0
                else:
                    # Adds the three numbers to our results and increments/decrements both l and r
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Loops so that l is not just a duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        # Returns the final array          
        return res