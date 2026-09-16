class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:

                for j in range(len(needle)):
                    if i + j >= len(haystack):
                        break

                    if haystack[i + j] != needle[j]:
                        break
                else:
                    return i

        return -1

solution = Solution()
print(solution.strStr("hello", "ll"))