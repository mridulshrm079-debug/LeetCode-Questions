class Solution(object):
    def findMaxLength(self, nums):
        prefix = 0
        max_length = 0

        # prefix_sum : first index where it appeared
        check = {0: -1}

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in check:
                max_length = max(max_length, i - check[prefix])
            else:
                check[prefix] = i

        return max_length