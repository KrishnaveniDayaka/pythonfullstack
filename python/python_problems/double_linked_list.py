
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        #Dll empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        #Dll is not empty
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        #Dll is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        #Dll is not empty
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
    def insert_at_position(self,data,position):
        if position<0:
            print("Invalid position")
            return
        if position==0:
            self.insert_at_begin(data)
            return

        #if position greater than zero (0)
        new_node=Node(data)
        temp=self.head
        for _ in range(position-1):
            if temp is None:
                print("Invalid position")
                return
            temp=temp.next
        new_node.next=temp.next
        new_node.prev=temp

        #Dll specific postion at end 
        if temp.next is not None:
            temp.next.prev=new_node
        else:
            self.tail=new_node
        temp.next=new_node

    def delete_at_begin(self):
        #Dll is empty
        if self.head is None:
            print("Double Linked List is empty")
            return
        #Dll has only one element
        if self.head==self.tail:
            self.head=None
            self.tail=None
        #Dll is not empty
        self.head=self.head.next
        self.head.prev=None

    def delete_at_ending(self):
        #Dll is empty
        if self.head is None:
            print("Double Linked List is empty")
            return
        #Dll has only one element
        if self.head==self.tail:
            self.head=None
            self.tail=None
        #Dll is not empty list
        self.tail=self.tail.prev
        self.tail.next=None
    def delete_by_value(self,value):

        if self.head is None:
            print("List is empty")
            return
        temp=self.head
        while temp is not None:
            if temp.data==value:
                if temp==self.head:
                    self.delete_at_begin()
                    return
                if temp==self.tail:
                    self.delete_at_ending()
                    return
                temp.prev.next=temp.next
                temp.next.prev=temp.prev
                return
            temp=temp.next
        print("Value not found")

    def delete_at_position(self,position):
        if self.head is None:
            print("List is empty")
            return
        if position<0:
            print("Invalid")
            return
        if position==0:
            self.delete_at_begin()
        temp=self.head
        for _ in range(position):
            temp=temp.next
        temp.prev.next=temp.next
        temp.next.prev==temp.prev

    def update(self,index,new_value):
        if index<0:
            return False
        temp=self.head
        count=0
        while temp is not None:
            if count==index:
                temp.data=new_value
                return True
            temp=temp.next
            count+=1
        return False
    def search(self,value):
        temp=self.head
        index=0
        while temp is not None:
            if temp.data==value:
                return index
            temp=temp.next
            index+=1
        return -1
    def reverse(self):
        temp=self.head
        while temp is not None:
            temp.prev,temp.next=temp.next,temp.prev
            temp=temp.prev
        self.head,self.tail=self.tail,self.head
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" <-> ")
            temp=temp.next
        print("None")
dll=DoublyLinkedList()
dll.insert_at_begin(10)

dll.insert_at_end(30)
dll.display()
dll.insert_at_position(20,1)
dll.display()
dll.insert_at_end(5)
dll.display()
dll.insert_at_begin(5)
dll.display()
dll.delete_at_begin()
dll.display()
dll.delete_at_ending()
dll.display()
dll.reverse()
dll.display()


