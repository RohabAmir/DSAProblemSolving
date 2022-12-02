# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        temp=head #pointing at the head of linkedlist
        x=0
#traversing over the entire linkedlist
        while temp is not None:
            x+=temp.val
            x*=2
            temp=temp.next
        return x/2
    