class Solution(object):
    def moveZeroes(self, nums):
        temp = 0
        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0:
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp

                slow = slow + 1

        return nums
        