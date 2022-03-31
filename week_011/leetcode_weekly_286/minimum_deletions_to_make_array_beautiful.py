from itertools import groupby

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        
        # initial values
        idx = 0
        n_deletions = 0
        
        for key, group in groupby(nums):
            group = list(group)

            if len(group) > 1:
                n_deletions += len(group) - 1 - ((idx - n_deletions) % 2 != 0)
            idx += len(group)
            
        len_array_with_deletions = len(nums) - n_deletions
        return n_deletions + 1 if len_array_with_deletions % 2 == 1 else n_deletions
