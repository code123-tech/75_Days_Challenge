
class Solution:
    def detectCycle(self, head):
        slow = fast = head
        isLoopExist = False
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if(slow == fast):
                isLoopExist = True
                break
        if isLoopExist:
            if(slow == head):
                return slow
            else:
                slow1 = head
                while slow.next != slow1.next:
                    slow = slow.next
                    slow1 = slow1.next
                return slow.next
        else:
            return None
