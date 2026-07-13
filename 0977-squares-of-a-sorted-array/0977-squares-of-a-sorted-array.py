class Solution(object):
    def sortedSquares(self, nums):
        i = 0
        j = len(nums) - 1
        result = []

        while i <= j:
            result.append(nums[i]*nums[i])
            if i != j:
                result.append(nums[j]*nums[j])
            i = i + 1
            j = j - 1

        ans = sorted(result)

        return ans

        