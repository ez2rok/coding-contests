from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        # initial value
        num_to_freq = Counter(tasks)        
        n_operations = 0
        
        
        for num, freq in num_to_freq.items():
            
            # base case:
            if freq == 1:
                return -1
            
            # if freq is odd
            if freq % 2 == 1:
                n_operations += 1
                freq -= 3
             
            # if freq is greater than 6 (and is even)
            if freq >= 6:
                n_operations += 2 * (freq // 6)
                freq = freq % 6
                
            # now we know freq is less than 6 and is even
            if freq == 4:
                n_operations += 2
            elif freq == 2:
                n_operations += 1
                
        return n_operations
        
