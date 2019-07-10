class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self,data):
        self.data = data
    
    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

class LinkedList():
    def __init__(self,head=None):
        self.head = head

    #insert at the begining of the linked list
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    #Inserts at the end of the linked list
    def append(self,data):
        new_node = Node(data)

        if self.head != None:
            node = self.head

            while node.next != None:
                node = node.next

            node.set_next(new_node)

        else:
            self.head = new_node
    
    #Print every single value of every node in the linked list
    def traverse(self):
        cadena = ""
        node = self.head
        while node != None:
            cadena+= str(node.data) + " "
            node = node.next
        
        print(cadena)
    
    #returns the size of the linked list
    def size(self):
        count = 0
        node = self.head
        while node != None:
            count+=1
            node = node.next
        
        return count
            


linked = LinkedList()
linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.traverse()
print(linked.size())
