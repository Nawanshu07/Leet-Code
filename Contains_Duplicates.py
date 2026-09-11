class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 1])        
print(result)