# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lst = []
        start = head
        while start:
            lst.append(start)
            start = start.next
        if(len(lst) < n):
            return head
        if(len(lst) == n and len(lst) > 1):
            head = lst[1]
            return head
        if(len(lst) == n and len(lst) == 1):
            return None
        lst[-n-1].next = lst[-n].next
        return head


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
print(sol.removeNthFromEnd(l1, 2))
