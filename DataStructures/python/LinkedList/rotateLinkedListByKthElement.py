 # https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1#
 #Input:
# N = 5
# value[] = {2, 4, 7, 8, 9}
# k = 3
# Output: 8 9 2 4 7
# Explanation:
# Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
# Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
# Rotate 3: 8 -> 9 -> 2 -> 4 -> 7
 
 
 #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        # treverse till kth element and keep its reference
        # treverse to tail
        # set tail next to head and kth element reference to null
        
        if k == 0:
            return head
            
        kthElement = None
        count = 1
        
        temp = head
        
        while (temp.next is not None):
            if count == k:
                kthElement = temp
            temp = temp.next
            count += 1
          
        if count <= k:
            #kth element is last
            return head
            
        newHead = kthElement.next  
        tail = temp
        tail.next = head
        kthElement.next = None
        
        return newHead