class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            digit_sum = 0
            n = nums[i]
            while n > 0:
                digit_sum += n % 10
                n //= 10
            if digit_sum == i:
                return i
        return -1

sol = Solution()
print(sol.smallestIndex([1, 3, 2]))
