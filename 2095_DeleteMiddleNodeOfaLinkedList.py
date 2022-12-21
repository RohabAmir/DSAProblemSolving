# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        prev=None
        slow=head
        fast=head
        while(fast and fast.next):
            prev=slow #It will help us in deleting the middle node
            slow=slow.next
            fast=fast.next.next
        if(prev):
            prev.next=slow.next
        else:
            head=None
        return head