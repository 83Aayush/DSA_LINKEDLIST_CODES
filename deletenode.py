class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty!")
            return
        self.head = self.head.next
        print("Node deleted from beginning.")

    def delete_from_end(self):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        print("Node deleted from end.")

    def display(self):
        if self.head is None:
            print("List is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Original List:")
ll.display()

ll.delete_from_beginning()
print("After deleting from beginning:")
ll.display()

ll.delete_from_end()
print("After deleting from end:")
ll.display()
