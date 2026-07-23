class Solution(object):
    def subarraySum(self, nums, k):
        total = 0
        new = []
        ans = 0

        hashmap = {0:1}
        for i in nums:
            total = total + i
            new.append(total)

        for i in new:
            if i - k in hashmap:
                ans = ans + hashmap[i - k]

            if i in hashmap:
                hashmap[i] = hashmap[i] + 1 
            else:
                hashmap[i] = 1

        return ans


        