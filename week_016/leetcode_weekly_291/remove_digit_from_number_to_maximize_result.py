class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        idxs = [i for i, n in enumerate(number) if n == digit]
        max_number = max([int(number[0:idx] + number[idx + 1:]) for idx in idxs])
        return str(max_number)
        
        
