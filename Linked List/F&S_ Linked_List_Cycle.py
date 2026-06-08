## Definition for singly-linked list. Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False



n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n4.next = n2

head = n1

sol = Solution()

result = sol.hasCycle(head)
print(result)


        
