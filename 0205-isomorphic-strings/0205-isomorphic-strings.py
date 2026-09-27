class Solution(object):
    def isIsomorphic(self, s, t):
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                hashmap[s[i]] = t[i]

        temp = {}
        for i in range(len(t)):
            if t[i] in temp:
                if temp[t[i]] != s[i]:
                    return False
            else:
                temp[t[i]] = s[i]
            
        return True

        