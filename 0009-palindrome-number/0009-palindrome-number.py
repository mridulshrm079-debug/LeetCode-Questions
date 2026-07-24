class Solution(object):
    def isPalindrome(self, x):
        if x == 0:
            return True
        temp = 0
        if x > 0:
            temp = str(x)
            result = int(temp[::-1])
            if x == result:
                return True
            else:
                return False
        else:
            return False
        