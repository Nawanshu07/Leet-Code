class Solution(object):
    def reversePrefix(self, s, k):
        return s[:k][::-1] + s[k:]

sol = Solution()
print(sol.reversePrefix("abcdef", 3))
