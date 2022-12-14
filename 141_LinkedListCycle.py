# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hare=head #FastSpeed
        tortoise=head #SlowSpeed
        while(hare and hare.next):
            tortoise=tortoise.next
            hare=hare.next.next
            if(tortoise==hare):
                return True
        return False