class Solution(object):
    def majorityElement(self, nums):
        majority = len(nums) // 2
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

            if count[i] > majority:
                return i

solution = Solution()
result = solution.majorityElement([3, 2, 3])
print(result)