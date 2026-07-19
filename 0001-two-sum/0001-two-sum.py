class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i in range(len(nums)):
            if target - nums[i] in check:
                return check[target - nums[i]], i
            else:
                check[nums[i]] = i


        