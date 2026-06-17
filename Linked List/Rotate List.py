# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
            
        curr = head
        len = 0
        
        while curr:
            curr = curr.next
            len+=1
        curr = head

        k = k % len

        if k == 0:
            return head
        
        curr = head

        for _ in range(len-k-1):
            curr = curr.next
        new_head = curr.next
        
        tail = new_head
            
        while tail.next:
            tail = tail.next
            
        tail.next = head
        curr.next = None
        return new_head
        
            
        
