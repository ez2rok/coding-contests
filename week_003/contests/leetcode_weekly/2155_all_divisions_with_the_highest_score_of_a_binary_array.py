class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        
        # create cumlative sum array where ith element is the sum of elements 0 through i, inclusive.
        cum_sum = []
        sum_ = 0
        for n in nums:
            sum_ += n
            cum_sum.append(sum_)
        
        # initialize via the edge cases partition_idx = 0
        max_division_score = cum_sum[-1]
        division_score_indicies = [0]
            
        
        for partition_idx, cs in enumerate(cum_sum):
            
            # compute division score
            left_score = partition_idx + 1 - cum_sum[partition_idx]
            right_score = cum_sum[-1] - cum_sum[partition_idx]
            division_score = left_score + right_score
            
            # update max division score, division_score_indicies
            if division_score > max_division_score:
                max_division_score = division_score
                division_score_indicies = []
            if max_division_score == division_score:
                division_score_indicies.append(partition_idx + 1)              
        
        return division_score_indicies
