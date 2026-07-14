class Solution(object):
    def isSubsequence(self, s, t):
        slow = 0
        if len(s) == 0:
            return True

        for i in range(len(t)):
            if s[slow] == t[i]:
                slow = slow + 1
                if slow == len(s):
                    return True

        return False

        