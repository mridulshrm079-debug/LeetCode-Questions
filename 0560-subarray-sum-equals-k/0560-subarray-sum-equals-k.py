class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        sum = 0
        prefix_sum = []
        for i in nums:
            sum = sum + i
            prefix_sum.append(sum)

        check = {0:1}

        for i in prefix_sum:
            if i - k in check:
                count = count + check[i-k]
            
            if i in check:
                check[i] = check[i] + 1
            else:
                check[i] = 1

        return count
        