# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev=None
        curr=head
        while curr:
            next=curr.next #save the future value as next
            curr.next=prev #pointing the link to previous node
            prev=curr # Make  previous node the current node
            curr=next #shift the current node to the next node
        return prev