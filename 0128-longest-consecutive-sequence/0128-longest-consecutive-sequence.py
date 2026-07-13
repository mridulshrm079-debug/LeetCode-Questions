class Solution(object):
    def longestConsecutive(self, nums):

        if not nums:
            return 0

        temp = sorted(set(nums))

        count = 1
        max_length = 1

        for i in range(1, len(temp)):
            if temp[i] == temp[i - 1] + 1:
                count += 1
            else:
                count = 1

            max_length = max(max_length, count)

        return max_length