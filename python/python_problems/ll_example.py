
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Insert at position
    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position - 1):
            if temp is None:
                print("Invalid position")
                return

            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete at beginning
    def delete_at_begininng(self):
        # List is empty
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        self.head = self.head.next

    # Delete at end
    def delete_at_ending(self):
        # List is empty
        if self.head is None:
            print("List is empty")
            return

        # Only one node
        if self.head.next is None:
            self.head = None
            return

        # More than one node
        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None

    # Delete by value
    def delete_by_value(self, value):
        # List is empty
        if self.head is None:
            print("List is empty")
            return

        # Value is in first node
        if self.head.data == value:
            self.head = self.head.next
            return

        # Search for value
        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                return

            temp = temp.next

        print("Value not found")

    # Delete at position
    def delete_at_position(self, position):
        # List is empty
        if self.head is None:
            print("List is empty")
            return

        # Negative position
        if position < 0:
            print("Invalid position")
            return

        # Position 0
        if position == 0:
            self.head = self.head.next
            return

        temp = self.head

        # Move to node before required position
        for _ in range(position - 1):
            if temp.next is None:
                print("Invalid position")
                return

            temp = temp.next

        # Position doesn't exist
        if temp.next is None:
            print("Invalid position")
            return

        # Delete node
        temp.next = temp.next.next

    # Search
    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.data == value:
                return True

            temp = temp.next

        return False

    # Length
    def length(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    # Reverse
    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # Check cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Display
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")
ll=LinkedList()
ll.insert_at_begin(10)
ll.display()