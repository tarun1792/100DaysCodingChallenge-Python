    def detectLoop(self, head):
        #code here
        
        slowPointer = head
        fastPointer = head
            
        while fastPointer and slowPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
            
        return False