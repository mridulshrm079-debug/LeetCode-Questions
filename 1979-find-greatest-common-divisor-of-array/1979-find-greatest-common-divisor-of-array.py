import fractions

class Solution(object):
    def findGCD(self, nums):
        result =  fractions.gcd(min(nums), max(nums))
        return result