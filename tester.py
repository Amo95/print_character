class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.head = Node()
        current = self.head
        print(current.next)

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_node(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

node1 = Node()
node1.data = "James"
datum = [i for i in range(1,10)]
link = LinkedList()
for i in datum:
    link.append(i)

link.print_node()
