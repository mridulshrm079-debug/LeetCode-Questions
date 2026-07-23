class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for i in nums1:
            found = False
            for j in range(len(nums2)):
                if i == nums2[j]:
                    if j == len(nums2) - 1:
                        result.append(-1)
                    else:
                        for k in range(j+1, len(nums2)):
                            if nums2[k] > i:
                                result.append(nums2[k])
                                found = True
                                break

                        if found == False:
                            result.append(-1)

        return result
        