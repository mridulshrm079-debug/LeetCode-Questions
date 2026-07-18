class Solution(object):
    def backspaceCompare(self, s, t):
        r_s = []
        t_s = []

        for i in s:
            if i == "#":
                if r_s:
                    r_s.pop()
            else:
                r_s.append(i)

        for i in t:
            if i == "#":
                if t_s:
                    t_s.pop()
            else:
                t_s.append(i)

        if r_s == t_s:
            return True
        else:
            return False

        