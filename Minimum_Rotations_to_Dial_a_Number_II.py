class Solution(object):
    def minRotations(self, n, s):
        total = 0
        prev = 0
        for ch in s:
            curr = int(ch)
            diff = abs(curr - prev)
            total += min(diff, n - diff)
            prev = curr
        return total

sol = Solution()
print(sol.minRotations(10, "246"))
