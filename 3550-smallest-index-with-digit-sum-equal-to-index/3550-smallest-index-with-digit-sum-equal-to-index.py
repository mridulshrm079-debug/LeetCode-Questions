class Solution(object):
    def smallestIndex(self, nums):
        sum = 0
        res = len(nums)
        for i in range(len(nums)):
            sum = 0
            for j in str(nums[i]):
                sum = sum + int(j)

            if sum == i:
                res = min(res, sum)
    
        if res == len(nums):
            return -1
        else:
            return res
        