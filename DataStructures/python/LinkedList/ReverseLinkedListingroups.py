# Reverse a Linked List in groups of given size.
# Input:
# LinkedList: 1->2->2->4->5->6->7->8
# K = 4
# Output: 4 2 2 1 8 7 6 5 
# Explanation: 
# The first 4 elements 1,2,2,4 are reversed first 
# and then the next 4 elements 5,6,7,8. Hence, the 
# resultant linked list is 4->2->2->1->8->7->6->5.

def reverse(self,head, k):  
        if head == None:
            return None
            
        currentNode  = head
        previousNode = None
        next = None
        count = 0
        
        while currentNode and count < k:
            next = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = next
            count += 1
            
        if next is not None:
            head.next = self.reverse(next,k)
            
        return previousNode