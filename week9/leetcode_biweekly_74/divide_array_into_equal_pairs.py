from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        val_to_freq = defaultdict(int)
        for n in nums:
            val_to_freq[n] += 1
        
        n_non_duals = len([freq for freq in val_to_freq.values() if freq % 2 != 0])
        return n_non_duals == 0
        
