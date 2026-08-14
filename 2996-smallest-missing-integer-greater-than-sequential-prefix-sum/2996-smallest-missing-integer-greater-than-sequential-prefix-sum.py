class Solution(object):
    def missingInteger(self, nums):
        if len(nums) == 1:
            return nums[0] + 1
        sum = nums[0]
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i + 1]:
                sum = sum + nums[i + 1]
            else:
                if sum in nums:
                    for i in nums:
                        if sum + 1 in nums:
                            sum = sum + 1
                        else:
                            return sum + 1
                else:
                    return sum

        return sum
    
        
        
        