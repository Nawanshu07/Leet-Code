class Solution(object):
    def runningSum(self, nums):
        sum = 0
        l = []
        for i in range(0,len(nums)):
            sum = sum + nums[i]
            l.append(sum)
        return l

solution = Solution()
result = solution.runningSum([1,2,3,4,5]) 
print(result)