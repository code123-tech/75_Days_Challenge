# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = reverse
            reverse = temp
        # if list have odd length then check for fast pointer if it is ended or not.
        if fast:
            slow = slow.next

        while reverse and slow and reverse.val == slow.val:
            reverse = reverse.next
            slow = slow.next

        return True if not reverse else False


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
print(sol.isPalindrome(l1))
