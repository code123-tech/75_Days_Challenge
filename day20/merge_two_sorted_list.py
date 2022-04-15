# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def merge(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        while True:

            if l1 is None:

                tail.next = l2
                break

            if l2 is None:

                tail.next = l1
                break

            if l1.val > l2.val:

                tail.next = l2
                l2 = l2.next

            else:

                tail.next = l1
                l1 = l1.next

            tail = tail.next

        return dummy.next

    def mergeTwoLists(self, l1, l2):

        if l1 is None and l2 is None:
            return None

        return self.merge(l1, l2)


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print(sol.mergeTwoLists(l1, l2))
