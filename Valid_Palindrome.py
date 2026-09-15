class Solution(object):
    def isPalindrome(self, s):
        a = ""
        for i in s:
            if i.isalnum():
                a+=i.lower()

        if a == a[::-1]:
            return True
        else:
            return False
        
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: True