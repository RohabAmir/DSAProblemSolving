# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if(list1==None): return list2
        if(list2==None): return list1
        curr=dummy= ListNode(0)
        while list1!=None and list2!=None:
            if(list1.val > list2.val):
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next #updating position of curr
        if(list1==None):
            curr.next=list2
        else:
            curr.next=list1
        return dummy.next