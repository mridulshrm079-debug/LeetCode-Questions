class Solution(object):
    def removeElement(self, nums, val):
        slow = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[slow]
                nums[slow] = nums[i]
                nums[i] = temp

                slow = slow + 1

        return slow


        