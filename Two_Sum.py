class Solution(object):
    def twoSum(self, nums, target):
        """Return indices of the two numbers that add up to target.

        Uses a hash map to find the complement in one pass.
        Time complexity: O(n) average; space complexity: O(n).
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
