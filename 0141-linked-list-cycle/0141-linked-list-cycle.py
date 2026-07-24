# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        list = []
        curr = head
        while curr:
            if curr.next in list:
                return True
            else:
                list.append(curr.next)

            curr = curr.next

        return False
        