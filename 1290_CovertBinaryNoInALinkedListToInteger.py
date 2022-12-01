# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        temp=head #pointing at the head of linkedlist
        x=0
        while temp is not None:
            x+=temp.val
            x*=10
            temp=temp.next
        return x/10