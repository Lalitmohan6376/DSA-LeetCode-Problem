class Solution:
    def detectCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next

        return curr
