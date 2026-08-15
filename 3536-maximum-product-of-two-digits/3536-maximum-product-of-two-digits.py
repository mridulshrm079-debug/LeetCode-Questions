class Solution(object):
    def maxProduct(self, n):
        temp = []
        for i in str(n):
            temp.append(int(i))
        temp.sort()

        return temp[-1] * temp[-2]