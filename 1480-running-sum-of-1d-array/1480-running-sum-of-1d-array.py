class Solution(object):
    def runningSum(self, nums):
        temp = 0
        result = []

        for i in nums:
            temp = temp + i
            result.append(temp)

        return result

        