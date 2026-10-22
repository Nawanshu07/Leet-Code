class Solution(object):
    def maxAlternatingSum(self, nums):
        n = len(nums)
        # dp with states: 
        # pos_no_del = max alternating sum ending here at + position, no deletion used
        # neg_no_del = max alternating sum ending here at - position, no deletion used
        # pos_del = max alternating sum ending here at + position, one deletion used
        # neg_del = max alternating sum ending here at - position, one deletion used
        
        pos_no_del = float('-inf')
        neg_no_del = float('-inf')
        pos_del = float('-inf')
        neg_del = float('-inf')
        
        result = float('-inf')
        
        for i in range(n):
            new_pos_no_del = max(nums[i], neg_no_del + nums[i])
            new_neg_no_del = pos_no_del - nums[i]
            
            # deletion used: either we deleted current element or a previous one
            new_pos_del = max(neg_del + nums[i], neg_no_del)  # delete current (skip from neg) or used deletion before
            new_neg_del = max(pos_del - nums[i], pos_no_del)  # delete current (skip from pos) or used deletion before
            
            # Also: start fresh with deletion already used (deleted some element before this subarray)
            new_pos_del = max(new_pos_del, nums[i])
            
            pos_no_del = new_pos_no_del
            neg_no_del = new_neg_no_del
            pos_del = new_pos_del
            neg_del = new_neg_del
            
            result = max(result, pos_no_del, neg_no_del, pos_del, neg_del)
        
        return result

sol = Solution()
print(sol.maxAlternatingSum([5,4,8,3]))
