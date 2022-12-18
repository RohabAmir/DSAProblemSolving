# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        #Base Condition
        if not head or not head.next:
            return head 


#Recursive Call
        newHead=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return newHead