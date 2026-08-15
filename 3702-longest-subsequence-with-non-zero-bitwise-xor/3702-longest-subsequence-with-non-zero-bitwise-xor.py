class Solution(object):
    def longestSubsequence(self, nums):
        total = 0

        for i in nums:
            total = total ^ i

        if total != 0:
            return len(nums)

        for i in nums:
            if i != 0:
                return len(nums) - 1

        return 0