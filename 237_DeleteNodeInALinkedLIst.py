# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
#If we need to delete the node without accessing the head, its not possible so we need to delete the next node
#At first copy the value of the next node in the given node
        temp=node
        temp=temp.next
        while(temp.next):
            node.val=temp.val
            node=temp
            temp=temp.next
        #Delete temp
        node.val=temp.val
        node.next=None

