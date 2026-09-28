class Solution(object):
    def maxDepth(self, s):
        count = 0
        l = []
        for i in s:
            if i== "(":
                count+=1
                l.append(count)
            elif i == ")":
                count-=1
                l.append(count)
        return max(l) if l else 0

sol = Solution()
print(sol.maxDepth("(1+(2*3)+((8)/4))+1"))