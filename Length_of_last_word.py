class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        return len(a[-1])

solution = Solution() 
print(solution.lengthOfLastWord("hi  my    name is nawanshuuu  "))