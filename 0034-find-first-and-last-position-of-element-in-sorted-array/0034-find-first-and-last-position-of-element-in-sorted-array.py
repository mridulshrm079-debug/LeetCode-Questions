class Solution(object):
    def searchRange(self, nums, target):

        i = 0
        j = len(nums) - 1

        while i <= j:

            mid = (i + j) // 2

            if nums[mid] < target:
                i = mid + 1

            elif nums[mid] > target:
                j = mid - 1

            else:

                left = mid
                right = mid

                while left > 0 and nums[left - 1] == target:
                    left -= 1

                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1

                return [left, right]

        return [-1, -1]