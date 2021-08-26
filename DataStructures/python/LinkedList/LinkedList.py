class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next  

    def insertFirst(self,data):
        # create the node
        node = Node(data)

        # Check if the head is null
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def insertLast(self,data):
        node = Node(data)
        # Check if the head is null then set the new node as head
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = node

    def deleteNode(self,key):

        temp = self.head

        if temp.data == key:
            self.head = temp.next
            return

        while(temp):
            if temp.next.data == key:
                temp.next = temp.next.next
                print("deleted the value ", key)
                break
            temp = temp.next        


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.printList()
    print("------- Pushed Nodes ----------")
    llist.insertFirst(0)
    llist.insertLast(4)
    llist.printList()
    print("------- Delete Node ----------")
    llist.deleteNode(3)
    llist.printList() 

