# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# 
# 
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        c = ListNode()
        head = c
        carryForward = 0
        
        while( a is not None) and (b is not None):
            sum = a.val + b.val + carryForward
            val = int(sum % 10)
            carryForward = int(sum / 10)
            c.next = ListNode(val)
            a = a.next
            b = b.next
            c = c.next
            
            
        while(a is not None):
            sum = a.val + carryForward
            val = int(sum % 10)
            carryForward = int(sum / 10)
            c.next = ListNode(val)
            a = a.next
            c = c.next
        
        while(b is not None):
            sum = b.val + carryForward
            val = int(sum % 10)
            carryForward = int(sum / 10)
            c.next = ListNode(val)
            b = b.next
            c = c.next
            
        if carryForward > 0:
            c.next = ListNode(carryForward)
            
            
        return head.next
    