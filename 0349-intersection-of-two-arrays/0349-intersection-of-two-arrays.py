class Solution(object):
    def intersection(self, nums1, nums2):
        result = []

        check1 = list(set(nums1))
        check2 = list(set(nums2))

        for i in range(len(check1)):
            if check1[i] in check2:
                result.append(check1[i])

        return result
        