class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")

        itr = self.head
        while itr:
            itr = itr.next

