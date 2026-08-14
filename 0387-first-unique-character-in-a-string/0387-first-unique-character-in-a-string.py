class Solution(object):
    def firstUniqChar(self, s):
        hashmap = {}
        for i in s:
            if i in hashmap:
                hashmap[i] = hashmap[i] + 1
            else:
                hashmap[i] = 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i

        return -1
        