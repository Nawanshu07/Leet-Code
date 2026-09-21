class Solution(object):
    def longestCommonPrefix(self, strs):
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre   

solution = Solution()
print(solution.longestCommonPrefix(["name" , "name" , "name"]))