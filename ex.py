# remove, size, peek, push, is_empty
class Stack:
    
    def __init__(self):
        self.items = list()
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        return self.items.append(item)

    def reverse(self):
        return "".join(self.items[::-1])
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

        
stack = Stack()
for i in "yesterday":
    stack.push(i)

print(stack.reverse())
