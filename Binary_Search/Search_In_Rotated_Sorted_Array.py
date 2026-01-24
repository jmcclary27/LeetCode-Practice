class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            print(R)
            if nums[L] == target: 
                return L
            if nums[R] == target: 
                return R
            if L == R and nums[L] != target: 
                return -1

            mid = L + ((R-L)//2)
            if nums[mid] == target: return mid

            if nums[mid] > target and nums[0] > target and nums[mid] > nums[0]:
                L = mid + 1
            
            elif nums[mid] < target and nums[len(nums) - 1] < target and nums[mid] < nums[len(nums) - 1]:
                R = mid - 1
            
            elif nums[mid] > target:
                R = mid - 1
            
            else:
                L = mid + 1
        
        return -1