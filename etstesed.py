class Node :
    def __init__(self, value) :
        self.head = value
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = None
        self.next = None
    
    def add_node(self, value, edges) :
        self.head = value
        
        for edge in edges :
            print(edge)
            if value == edge[0] : self.next = edge[1]
            elif value == edge[1] : self.next = edge[0]
            print(self.head)
            print(self.next)
            

nnn = LinkedList()
nnn.add_node(3, [[1, 2], [2, 3]])
print(nnn)