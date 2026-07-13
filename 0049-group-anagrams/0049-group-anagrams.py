class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp in dict:
                dict[temp].append(i)
            else:
                dict[temp] = [i]

        result = []
        for i in dict:
            result.append(dict[i])

        return result
        