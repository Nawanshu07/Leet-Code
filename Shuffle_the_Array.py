class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result

sol = Solution()
print(sol.shuffle([2, 5, 1, 3, 4, 7], 3))
