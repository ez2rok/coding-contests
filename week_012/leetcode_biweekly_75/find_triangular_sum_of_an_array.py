class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        new_nums = [(a + b) % 10 for a, b in zip(nums, nums[1:])]
        return self.triangularSum(new_nums)
        
