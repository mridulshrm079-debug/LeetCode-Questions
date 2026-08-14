class Solution(object):
    def maximumLengthSubstring(self, s):
        maxi = 0
        for i in range(len(s)):
            hashmap = {}
            count = 0
            for j in range(i, len(s)):
                if s[j] in hashmap:
                    hashmap[s[j]] = hashmap[s[j]] + 1
                else:
                    hashmap[s[j]] = 1
                
                if hashmap[s[j]] <= 2:
                    count = count + 1
                else: 
                    break
            
            if maxi < count:
                maxi = count

        return maxi
            


        