class Solution(object):
    def missingNumber(self, nums):
        for i in range(0, max(nums)):
            if i not in nums:
                return i

        return max(nums) + 1
        