class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            
            new_s = ''
            for i in range(math.ceil(len(s) / k)):
                start = i * k
                end = min((i+1) * k, len(s))
                sum_ = sum([int(x) for x in s[start:end]])
                new_s += str(sum_)
                
            s = new_s            
        return s
