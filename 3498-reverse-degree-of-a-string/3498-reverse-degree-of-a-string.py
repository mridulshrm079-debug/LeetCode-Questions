class Solution(object):
    def reverseDegree(self, s):
        sum = 0
        for i in range(len(s)):
            sum = sum + ((123 - ord(s[i])) * (i+1))

        return sum
        