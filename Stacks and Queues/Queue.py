class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,val):
        self.queue.insert(0,val)
    
    def dequeue(self):
        if self.queue.is_empty():
            return None
        else:
            return self.queue.pop()
    
    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.queue.size() == 0

    def show(self):
        return self.queue
    
cola = Queue()
lista = [Queue()]
print(lista)
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)
print(cola.show())

