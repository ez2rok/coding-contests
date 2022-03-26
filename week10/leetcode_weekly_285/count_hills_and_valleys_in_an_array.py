from itertools import groupby

class Solution:
    
    def sign(self, x):
        return -1 if x < 0 else 1
    
    def countHillValley(self, nums: List[int]) -> int:
        
        signs = [self.sign(nums[i] - nums[i+1]) for i in range(len(nums) - 1) if nums[i] - nums[i+1] != 0]        
        sign_changes = sum([signs[i] != signs[i+1] for i in range(len(signs) - 1)])
        return sign_changes
