class Solution(object):
    def removeDuplicates(self, nums):
        temp = 0
        slow = 0

        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow + 1
                nums[slow] = nums[fast]

        return slow + 1