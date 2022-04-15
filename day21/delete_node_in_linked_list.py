# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        prev = None
        while node.next is not None:
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
sol.deleteNode(l1.next)
