class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    
    def rotate(self, nums: List[int], k: int) -> None:
        
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    
        
        
# O(1) space, O(n/k*k + k*k)=O(n+k^2) time      
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """  
        
#         # base case
#         if k == 0:
#             return nums
#         if k == len(nums):
#             return reversed(nums)
        
#         # initial values
#         k = k % len(nums)
#         pointer_idx = len(nums) - k
#         range_ = k  
            
        
#         # move the last n-k - n%k elements to the last n-k - n%k spots in the list.
#         # swap the last k elements with the second-to-last chunk of k elements,
#         # then swapt it with the third-to-last chunk of k elements, etc. Repeat
#         # until you have fewer than k elements that you can swap with -- this is
#         # the n%k elements.
#         while pointer_idx > k: #O(n / k)
            
#             # swap the last k elements with the second-to-last chunk of k elements
#             for i in range(pointer_idx, pointer_idx + k): # O(k)
#                 nums[i], nums[i - k] = nums[i - k], nums[i]
                
#             # move the pointer k elements back
#             pointer_idx = pointer_idx - k
#             #print('nums={}\t\tpointer={}, k={}'.format(nums, pointer_idx, k))
        
#         # swap the last n%k elements with the last k elements which at this point
#         # have been moved to the location [n%k, n%k + k]
#         if pointer_idx != 0:     
#             for offset2, i in enumerate(range(pointer_idx, pointer_idx + k)): #O(k)
#                 for offset1, j in enumerate(reversed(range(pointer_idx))): #O(k), pointer_idx=c-k for some constant c
#                     nums[i - offset1], nums[j + offset2] = nums[j + offset2], nums[i - offset1]
                
        
        
        
        # # O(n) time and space, not in place
        # result = [0] * len(nums)
        # for i, n in enumerate(nums):
        #     result[(i + k) % len(nums)] = n
        # print(result)
      
