# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # initial values
        left_idx, right_idx = 0, n
        
        while left_idx <= right_idx:
            
            middle_idx = left_idx + (right_idx - left_idx) // 2
            
            if not isBadVersion(middle_idx) and isBadVersion(middle_idx + 1):
                return middle_idx + 1
            
            if isBadVersion(middle_idx):
                right_idx = middle_idx - 1
            else:
                left_idx = middle_idx + 1
