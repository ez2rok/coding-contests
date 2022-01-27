class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        # remove max and min and all their duplicates
        min_ = min(nums)
        max_ = max(nums)
        
        nums2 = [n for n in nums if n != min_ and n != max_]
        return len(nums2) if nums2 else 0