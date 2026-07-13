class Solution(object):
    def isAnagram(self, s, t):
        dict = {}
        check = {}
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] = dict[s[i]] + 1
            else:
                dict[s[i]] = 1

        for i in range(len(t)):
            if t[i] in check:
                check[t[i]] = check[t[i]] + 1
            else:
                check[t[i]] = 1

        if check == dict:
            return True
        else:
            return False
        