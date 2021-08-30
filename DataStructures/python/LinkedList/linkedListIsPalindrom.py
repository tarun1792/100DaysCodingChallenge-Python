#https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/?company[]=Amazon&company[]=Amazon&problemType=functional&page=1&sortBy=submissions&query=company[]AmazonproblemTypefunctionalpage1sortBysubmissionscompany[]Amazon

#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        
        temp = head
        
        stack = []
        
        isPalindrome = 1
        
        while(temp is not None):
            stack.append(temp.data)
            temp = temp.next
            
        temp2 = head
        
        while(temp2 is not None):
            
            lastElement = stack.pop()
            
            if lastElement == temp2.data:
                isPalindrome = 1
            else:
                isPalindrome = 0
                break
            
            temp2 = temp2.next
            
        return isPalindrome