class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
                
        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(pos.pop(0))
            else:
                result.append(neg.pop(0))
                
        return result