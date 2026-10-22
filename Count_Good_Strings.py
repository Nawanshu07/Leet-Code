class Solution(object):
    def countGoodStrings(self, n):
        MOD = 10**9 + 7
        # A binary string that is a palindrome and has no two adjacent same chars
        # must alternate: "010101..." or "101010..."
        # For even n, "0101...01" reversed is "1010...10" which != original, so impossible
        # For odd n, both "01010...010" and "10101...101" are valid palindromes
        if n % 2 == 1:
            return 2
        else:
            return 0

sol = Solution()
print(sol.countGoodStrings(3))
