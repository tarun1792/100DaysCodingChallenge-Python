def findMid(head):
    # Code here
    # return the value stored in the middle node
    if head.next is None:
        return head.data
        
    ptr1 = head
    ptr2 = head
    
    while(ptr2.next is not None):
        ptr1 = ptr1.next
        if ptr2.next.next is not None:
            ptr2 = ptr2.next.next
        else: 
            break
        
    return ptr1.data