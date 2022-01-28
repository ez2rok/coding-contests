class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        # initial values
        right_idx = len(nums) - 1
        left_idx = 0
        result = [0] * len(nums)
        
        while left_idx <= right_idx:
            
            if abs(nums[left_idx]) < nums[right_idx]:
                result[right_idx - left_idx] = nums[right_idx] * nums[right_idx]
                right_idx -= 1
            else:
                result[right_idx - left_idx] = nums[left_idx] * nums[left_idx]
                left_idx += 1
                
        return result
                
        
        
      
    # SOLUTION WITH FINDING A PIVOT
#     def sortedSquares(self, nums: List[int]) -> List[int]:
                
#         # compute the pivot, the index where nums goes from positive to negative numbers
#         # specifically, it is the largest negative number; if all positive numbers, return 0
#         pivot_idx = [i for i, n in enumerate(nums) if n < 0]
#         pivot_idx = pivot_idx[-1] if pivot_idx else 0
        
#         # initial values
#         left_idx = pivot_idx
#         right_idx = pivot_idx + 1
#         result = []
        
        
#         # consider the numbers to the right and left of the pivot, one will be 
#         # positive one will be negative and take the smaller one, square it,
#         # add it to the results, and increase the index. 
#         while left_idx >= 0 and right_idx <= len(nums) - 1:
            
#             if abs(nums[left_idx]) > nums[right_idx]:
#                 result.append(nums[right_idx] ** 2)
#                 right_idx += 1
#             else:
#                 result.append(nums[left_idx] ** 2)
#                 left_idx -= 1
                
#         # if the rest of nums are positive
#         if left_idx == -1:
#             return result + [n ** 2 for n in nums[right_idx:]]
        
#         # if the rest of nums are negative
#         if right_idx == len(nums):
#             return result + [n ** 2 for n in nums[:left_idx + 1]][::-1]
        
