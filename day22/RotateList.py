# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):

        def getLinkedListLength():
            size = 0
            tail2 = head
            while tail2:
                size += 1
                if tail2.next is None:
                    break
                tail2 = tail2.next
            return [size, tail2]

        def recursive(current, prev):
            if current is None:
                return prev

            reverseHead = recursive(current.next, current)
            current.next = prev
            return reverseHead

        size, tail2 = getLinkedListLength()

        if size == 0 or k % size == 0:
            return head

        k = k % size

        head1 = head
        tail1 = head

        for i in range(size-k-1):
            tail1 = tail1.next

        head2 = tail1.next
        tail1.next = None

        tail1, tail2 = head1, head2

        head1 = recursive(head1, None)
        head2 = recursive(head2, None)
        tail1.next = head2

        return recursive(head1, None)
