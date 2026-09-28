class Solution(object):
    def maxDepth(self, s):
        count = 0
        res = 0
        for i in s:
            if i == "(":
                count = count + 1
                res = max(count, res)
            elif i == ")":
                count = count - 1

        return res
        