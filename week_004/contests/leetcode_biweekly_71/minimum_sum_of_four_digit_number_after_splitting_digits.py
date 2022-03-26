class Solution:
    def minimumSum(self, num: int) -> int:
        
        digits = [int(x) for x in str(num)]
        sorted_digits = sorted(digits)
        new1 = int(''.join(map(str, sorted_digits[::2])))
        new2 = int(''.join(map(str, sorted_digits[1::2])))
        return new1 + new2
        
