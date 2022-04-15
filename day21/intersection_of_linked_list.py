# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        first = headA
        sec = headB
        while first != sec:
            first = headB if first is None else first.next
            sec = headA if sec is None else sec.next

        return first


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
print(sol.getIntersectionNode(l1, l1.next.next))
