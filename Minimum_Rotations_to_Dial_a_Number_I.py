class Solution(object):
    def minRotations(self, s):
        total = 0
        prev = 0
        for ch in s:
            curr = int(ch)
            diff = abs(curr - prev)
            total += min(diff, 10 - diff)
            prev = curr
        return total

sol = Solution()
print(sol.minRotations("246"))
