class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        hashmap = {}

        for num in nums2:

            while stack and num > stack[-1]:

                smaller = stack.pop()
                hashmap[smaller] = num

            stack.append(num)

        while stack:
            hashmap[stack.pop()] = -1

        result = []

        for num in nums1:
            result.append(hashmap[num])

        return result