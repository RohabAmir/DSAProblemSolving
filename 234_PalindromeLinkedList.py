# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if ( head==None) or (head.next==None):
            return True
        slow,fast,curr,prev= head,head,head,None
        while(fast and fast.next):
            curr=slow
            slow=slow.next
            fast=fast.next.next
            curr.next=prev
            prev=curr
        #Condition for odd case
        if(fast):
            slow=slow.next
        while(prev):
            if(prev.val!=slow.val):
                return False
            else:
                prev=prev.next
                slow=slow.next
        return True

