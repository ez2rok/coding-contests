class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # initial values
        start_idx = 0
        end_idx = len(nums) - 1
        
        while end_idx >= start_idx:
            
            middle_idx = start_idx + (end_idx - start_idx) // 2
            middle_val = nums[middle_idx]
            
            if middle_val == target:
                return middle_idx
            
            if middle_val > target:
                end_idx = middle_idx - 1
            else:
                start_idx = middle_idx + 1
                
        return start_idx
        
