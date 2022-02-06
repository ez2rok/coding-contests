class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        is_negative = num < 0
        num = str(num)[1:] if is_negative else str(num)
        digits = [int(n) for n in str(num)]
        digits = sorted(digits, reverse=is_negative)
        n_zeros = sum([d == 0 for d in digits])
        if n_zeros and not is_negative:
            digits = [digits[n_zeros]] + digits[:n_zeros] + digits[n_zeros + 1:]
            
        num_str = [str(d) for d in digits]
        num_str = ['-'] + num_str if is_negative else num_str
        num = int(''.join(num_str))
        return num
