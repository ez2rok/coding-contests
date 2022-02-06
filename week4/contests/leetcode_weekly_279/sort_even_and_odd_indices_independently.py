class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even = [n for i, n in enumerate(nums) if i % 2 == 0]
        odd = [n for i, n in enumerate(nums) if i % 2 == 1]
        
        even_sorted = sorted(even, reverse=True)
        odd_sorted = sorted(odd)
        
        results = []
        while even_sorted or odd_sorted:
            if even_sorted:
                results.append(even_sorted.pop())
            if odd_sorted:
                results.append(odd_sorted.pop())
    
        return results
       
