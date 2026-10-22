class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for char in s + t:
            result ^= ord(char)
        return chr(result)

sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))
