class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#LinkedList class
class LinkedList:
    #creation of head
    def __init__(self):
        self.head=None
    #Displaying of linkedList
    def Display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end='-->') #end=' ' creates a white space instead of line break
            temp=temp.next
    #addition of node at begining
    def push(self,new_data):
        new_node=Node(new_data)  #creation of new node
        new_node.next=self.head  
        self.head=new_node
    #insertion after a given data
    def InsertAfter(self,given_node,new_data):
        if given_node is None: 
            print('The given node must be in LinkedList.')
            return
        new_node=Node(new_data)
        new_node.next=given_node.next
        given_node.next=new_node

    def InsertLast(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
           
        temp.next=new_node
        new_node.next=None

#instance of LinkedList
ll = LinkedList()

#creation of Nodes
ll.head = Node(1)
second = Node(2)
third = Node(3)

#linking the all nodes
ll.head.next = second
second.next = third
third.next = None

#before insertion at the beginning
print('\n before insertion at the beginning')
ll.Display()

#insertion at the begining
ll.push(5)

#display insertion at the beginning
print('\n After insertion at the beginning')
ll.Display()

#insertion after given node
ll.InsertAfter(ll.head.next.next, 8)

#display insertion after given node
print('\ninsertion after given node')
ll.Display()

print('\ninsertion at the last')
ll.InsertLast(9)
ll.Display()