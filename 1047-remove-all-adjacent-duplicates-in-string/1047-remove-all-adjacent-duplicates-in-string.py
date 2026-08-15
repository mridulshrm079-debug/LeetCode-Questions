class Solution(object):
    def removeDuplicates(self, s):
        temp = []
        res = ""
        for i in s:
            if temp:
                if i == temp[-1]:
                    temp.pop()
                else:
                    temp.append(i)
            else:
                temp.append(i)

        for i in temp:
            res = res + i
        
        return res



        