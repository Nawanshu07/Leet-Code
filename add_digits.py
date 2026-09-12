class Solution(object):
    def addDigits(self, num):

        while len(str(num))>1:
            n = sum(int(digit) for digit in str(num))
            num = n
        return num

solution = Solution()
result = solution.addDigits(38)
print(result)