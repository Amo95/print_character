class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
                print(f"data: {current.data}")
                
            current.next = Node(data)
            print(f"current next: {current.next}")

    def print_link(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Target found")
                return True
            else:
                current = current.next
        print("Target not found")
        return False


data = [i for i in range(1,10)]
link = LinkedList()
for i in data:
    link.append(i)

link.print_link()
link.search(53)
