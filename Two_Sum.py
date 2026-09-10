class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target :
                    result.extend([i,j])
        return result

a = Solution()
l = a.twoSum([2, 7, 11, 15], 9)
print(l)