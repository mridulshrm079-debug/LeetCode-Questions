class Solution(object):
    def maxProduct(self, nums):
        temp1 = max(nums)
        for i in range(len(nums)):
            if nums[i] == temp1:
                nums.pop(i)
                break
        
        temp2 = max(nums) - 1

        return (temp1 - 1) * temp2
        