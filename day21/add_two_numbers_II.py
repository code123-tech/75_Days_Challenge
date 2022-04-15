# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = self.reverse(l1)
        second = self.reverse(l2)
        newhead = tail = ListNode(-1)
        prev = 0
        while first and second:
            data = (first.val+second.val + prev) % 10
            prev = (first.val+second.val + prev)//10
            if(newhead.val == -1):
                newhead = ListNode(data)
                tail = newhead
            else:
                tail.next = ListNode(data)
                tail = tail.next
            first = first.next
            second = second.next
        if(prev > 0 and first is None and second is None):
            tail.next = ListNode(prev)
            tail = tail.next
            prev = 0
        while first:
            data = (first.val + prev) % 10
            prev = (first.val + prev)//10
            tail.next = ListNode(data)
            tail = tail.next
            first = first.next
        if(second is None and prev > 0):
            tail.next = ListNode(prev)
            tail = tail.next
            prev = 0
        while second:
            data = (second.val + prev) % 10
            prev = (second.val + prev)//10
            tail.next = ListNode(data)
            tail = tail.next
            second = second.next
        if(first is None and prev > 0):
            tail.next = ListNode(prev)
            tail = tail.next
            prev = 0
        return self.reverse(newhead)


sol = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(5)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)
print(sol.addTwoNumbers(l1, l2))
