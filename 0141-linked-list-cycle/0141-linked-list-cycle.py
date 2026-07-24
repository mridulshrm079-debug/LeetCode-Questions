# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        visit = set()
        curr = head
        while curr:
            if curr in visit:
                return True
            else:
                visit.add(curr)

            curr = curr.next

        return False
        