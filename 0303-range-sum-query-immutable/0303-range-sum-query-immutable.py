class NumArray(object):

    def __init__(self, nums):
        self.prefix = [0]
        total = 0
        for i in nums:
            total = total + i
            self.prefix.append(total)


    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)