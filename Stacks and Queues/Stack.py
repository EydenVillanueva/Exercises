 class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    
    def push(self, val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.size() == 0

    def show(self):
        return self.stack[::-1]

pila = Stack()
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)
pila.pop()
print(pila.show())