class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

n3 = ListNode(3)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)
head = n1

obj = Solution()
ans = obj.reverseList(head)
curr = ans

while curr:
    print(curr.val,end="-> ")
    curr = curr.next
print("None")
print(ans)
