class Solution(object):
    def shuffle(self, nums, n):
        result = []

        j = n

        for i in range(n):
            result.append(nums[i])
            result.append(nums[j])
            j = j + 1

        return result

        