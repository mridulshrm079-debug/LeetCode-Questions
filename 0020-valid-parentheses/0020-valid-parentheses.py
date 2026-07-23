class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:

            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            else:

                if not stack:
                    return False

                if stack[-1] != pairs[ch]:
                    return False

                stack.pop()

        return len(stack) == 0