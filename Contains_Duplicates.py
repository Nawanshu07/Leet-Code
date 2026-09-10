class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        maxx = 2
        for i , num in enumerate(nums):

            if num in count:
                count[num] = count.get(num,0) + 1
            else:
                count[num] = 1

        for i in nums:
            if count[i] >= 2:
                return True
        return False

solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 1])        
print(result)