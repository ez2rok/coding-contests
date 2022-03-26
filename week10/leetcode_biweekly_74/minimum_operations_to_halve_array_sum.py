from heapq import heappop, heappush, heapify

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        # initial values
        sum_ = sum(nums)
        threshold = sum_ / 2
        nums = [-1 * n for n in nums] # O(n); because heapq is a min-heap
        heapify(nums) # O(n)
        count = 0
        
        while sum_ > threshold:
            
            # pop max element, half it, and update sum
            max_elm = -1 * heappop(nums) # O(log n)
            max_elm /= 2
            sum_ -= max_elm
            
            # insert max_elm back into nums
            heappush(nums, -1 * max_elm) # O(log n)
            
            # update count
            count += 1
        return count
        
