class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = 1

        return False
        