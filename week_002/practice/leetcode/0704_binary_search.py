class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # initial values
        start_idx = 0
        end_idx = len(nums) - 1
        
        while end_idx >= start_idx: # why does this need to be or equal
            
            middle_idx = (end_idx - start_idx) // 2 + start_idx
            middle_val = nums[middle_idx]
            
            if middle_val == target:
                return middle_idx
            
            if middle_val > target:
                end_idx = middle_idx - 1
            else: # middle_val < target
                start_idx = middle_idx + 1
            
        return -1
