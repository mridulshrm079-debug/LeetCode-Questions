# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        list = []
        curr = head
        while curr:
            list.append(curr.val)
            curr = curr.next

        if list == list[::-1]:
            return True
        else:
            return False


        