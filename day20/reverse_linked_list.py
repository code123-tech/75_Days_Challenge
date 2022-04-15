# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        def recursive(current, prev):
            if current is None:
                return prev

            reverseHead = recursive(current.next, current)
            current.next = prev
            return reverseHead

        return recursive(head, None)


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print(sol.reverseList(l1))
