class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = 0

        for num in nums[:-1]:
            if num == 0 and counter == 0:
                return False
            if num > counter:
                counter = num
            counter -= 1
        return True