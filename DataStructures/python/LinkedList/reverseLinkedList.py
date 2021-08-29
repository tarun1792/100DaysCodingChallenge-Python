
#Function to reverse a linked list.
# Input:
# LinkedList: 1->2->3->4->5->6
# Output: 6 5 4 3 2 1
# Explanation: After reversing the list, 
# elements are 6->5->4->3->2->1.

    def reverseList(self, head):
        # Code here
        
        #algo
        current = head
        previous = None
        
        while(current is not None):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
    
        return previous