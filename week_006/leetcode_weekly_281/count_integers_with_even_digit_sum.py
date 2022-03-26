class Solution:    
    def countEven(self, num: int) -> int:      
        
        def sum_digits(x):
            return 0 if x == 0 else sum_digits(x // 10) + x % 10
        
        return sum([sum_digits(n) % 2 == 0 for n in range(1, num + 1)])
 
