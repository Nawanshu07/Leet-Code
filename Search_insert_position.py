class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i , num in enumerate(nums):
                if num > target:
                    return i
            else:
                return i+1
            

solution = Solution()
result = solution.searchInsert([1, 3, 5, 6], 7)
print(result)