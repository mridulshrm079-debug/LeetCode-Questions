class Solution(object):
    def isPalindrome(self, s):
        cleaned = "".join(i for i in s if i.isalnum()).lower()

        i = 0
        j = len(cleaned) - 1
        while i < j:
            if cleaned[i] != cleaned[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        
        return True


        