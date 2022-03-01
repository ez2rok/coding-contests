from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s = Counter(s)
        t = Counter(t)
        
        diff1 = s - t
        diff2 = t - s
        
        n_differences1 = sum(diff1.values())
        n_differences2 = sum(diff2.values())
        
        return n_differences1 + n_differences2
      
