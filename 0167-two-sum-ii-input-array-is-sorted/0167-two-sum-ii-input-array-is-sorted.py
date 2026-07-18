class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        sum = 0

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j = j - 1
            elif sum < target:
                i = i + 1
            else:
                return i + 1, j + 1
        