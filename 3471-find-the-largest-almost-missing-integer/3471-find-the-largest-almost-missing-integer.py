class Solution(object):
    def largestInteger(self, nums, k):
        if len(nums) == k:
            return max(nums)
        ans = []
        hashmap = {}
        check = []
        for i in range(len(nums) - (k - 1)):
            temp = []
            for j in range(i, i + k):
                temp.append(nums[j])
            check.append(temp)

        for i in check:
            for j in i:
                if j in hashmap:
                    hashmap[j] = hashmap[j] + 1
                else:
                    hashmap[j] = 1

        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1]))
        
        toggle = next(iter(hashmap.values()))
        for i in hashmap:
            if hashmap[i] == 1:
                ans.append(i)

        if ans:
            return max(ans)
        else:
            return -1


       
