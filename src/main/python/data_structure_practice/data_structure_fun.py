class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("previous Node not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if  current_node and current_node.data==key:
            self.head = current_node.next
            current_node = None
            return

        prev = None

        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            return

        prev.next = current_node.next
        current_node = None







llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.prepend("E")
llist.delete_node("A")

llist.insert_after_node(llist.head.next,"E")
#print(llist.head.data)
llist.print_list()
