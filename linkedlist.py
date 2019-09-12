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
            print(temp.data,end=' ') #end=' ' creates a white space instead of line break
            temp=temp.next

#instance of LinkedList
ll=LinkedList()

#creation of Nodes
ll.head=Node(1)
second=Node(2)
third=Node(3)

#linking the all nodes
ll.head.next=second
second.next=third
third.next=None

#calling the Display method
print('created LinkList is :', end=' ')
ll.Display()