class Solution(object):
    def threeSum(self, nums):
        result = []
        temp = sorted(nums)

        for i in range(len(temp)):
            check = set()

            for j in range(i + 1, len(temp)):
                need = -(temp[i] + temp[j])

                if need in check:
                    triplet = [temp[i], need, temp[j]]
                    if triplet not in result:
                        result.append(triplet)
                else:
                    check.add(temp[j])

        return result