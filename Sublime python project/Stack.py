# Stack
#a stack is a data structure that follows the Last In, First Out (LIFO) principle. It means that the last element added to the stack is the first one to be removed
#Push: Adds an element to the top of the stack.
# Pop: Removes the element from the top of the stack.
#a common operation is Peek (or Top): Inspects the element at the top of the stack without removing it
stack =  []
#Push an element to stack

for i in range(10):
    stack.append(i)
print(stack)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


    def size(self):
        return len(self.items)

stack = Stack()

stack.push(1)
stack.push(3)
stack.push(2)
stack.push(5)
stack.push(6)
stack.push(8)

print("Stack", stack.items)
print("peek", stack.peek())
print("pop", stack.pop())
print("stack after pop:", stack.items)