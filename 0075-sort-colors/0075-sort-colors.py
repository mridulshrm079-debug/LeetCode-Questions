class Solution(object):
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        temp = 0

        while mid <= high:
            if nums[mid] == 0:
                temp = nums[mid]
                nums[mid] = nums[low]
                nums[low] = temp

                low = low + 1
                mid = mid + 1

            elif nums[mid] == 2:
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp

                high = high - 1

            elif nums[mid] == 1:
                mid = mid + 1

        return nums
        