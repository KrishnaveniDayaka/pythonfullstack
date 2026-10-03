
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        new_node.next=self.head
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        #ll is empty
        if self.head is None:
            self.head=new_node
            return
        #ll is not empty
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
    def insert_at_position(self,data,position):
        if position <0:
            print("Invalid position")
            return
        if position==0:
            self.insert_at_begin(data)
            return
        new_node=Node(data)
        temp=self.head
        for i in range(position-1):
            if temp is None:
                print("Invalid position")
                return
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def delete_at_begininng(self):
        #ll is empty
        if self.head is None:
            print("List is empty")
        #ll has only one element
        if self.head.next is None:
            self.head=None
            return
        #ll is not empty
        self.head=self.head.next
    def delete_at_ending(self):
        #ll is empty
        if self.head is None:
            print("List is empty")
        if self.head.next is None:
            self.head=None
            return
        #ll as more than one element
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
    def delete_by_value(self,value):
        #ll is empty
        if self.head is None:
            print("List is empty")
            return
        if self.head.data==value:
            self.head=None
            return
        if self.head.data==value:
            self.head=self.head.next
        temp=self.head
        while temp.next is not None:
            if temp.next.data==value:
                temp.next=temp.next.next
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
            self.head=self.head.next
            return
        temp=self.head
        for _ in range(position-1):
            if temp.next is None:
                print("Invalid position")
                return 
            temp=temp.next
        if temp.next is None:
            print("Invalid position")
            return
        temp.next=temp.next.next
    def search(self,value):
        temp=self.head
        while temp is not None:
            if temp.data==value:
                return True
            temp=temp.next
        return False

    def length(self):
        count=0
        temp=self.head
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    def reverse(self):
        prev=None
        temp=self.head
        while temp is not None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.head=prev    
    def has_cycle(self):
        slow=self.head
        fast=self.head
        while slow.next and fast.next.next:
        #while fast is not none and fast.next is not none
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.data, end=" ->")
            temp=temp.next
        print("None")
ll= LinkedList()
ll.insert_at_begin(10)
ll.insert_at_end(20)
ll.insert_at_position(15,1)

ll.display() 
ll.delete_at_begininng()
ll.display()
ll.delete_at_ending()
ll.display()
ll.insert_at_end(50)
ll.display()
print("has cycles:",ll.has_cycle())

ll.reverse()
ll.display()
ll.delete_by_value(30)
ll.display()

print("Search element :",ll.search(5))

print("Has length :",ll.length())

            



    




   

