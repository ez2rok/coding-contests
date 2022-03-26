class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        # base case
        if finalSum % 2 == 1:
            return []
      
        # initial values
        i = 1
        results = [0]
        remaining_val = finalSum
        
        while remaining_val >= results[-1] + 2:
            results.append(results[-1] + 2)
            i += 1
            remaining_val -= results[-1]
        results[-1] += remaining_val  

        return results[1:]
            
