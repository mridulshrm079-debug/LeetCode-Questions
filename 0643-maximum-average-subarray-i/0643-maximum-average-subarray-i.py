class Solution(object):
    def findMaxAverage(self, nums, k):
        total = 0

        for i in range(k):
            total = total + nums[i]

        result = total

        for i in range(len(nums) - k):
            total = total - nums[i]
            total = total + nums[i + k]

            if total > result:
                result = total

        return float(result) / k

        