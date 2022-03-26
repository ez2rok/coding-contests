class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        count = 0
        for j in range(1, len(nums)):
            for i in range(j):
                if (i * j) % k ==0 and nums[i] == nums[j]:
                    count += 1
        return count
