class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # initial
        left_pointer = 0
        right_pointer = len(nums) - 1
        n_pivot_vals = 1
        
        before_pivot = [n for n in nums if n < pivot]
        after_pivot = [n for n in nums if n > pivot]
        pivot_vals = [n for n in nums if n == pivot]
        
        return before_pivot + pivot_vals + after_pivot
    
