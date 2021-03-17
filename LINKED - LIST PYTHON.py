# Create Node ( one is for element and onter is for address)
class Node:
    def __init__(self,data):
        self.element = data
        self.next = None
        
# Create Head element as NULL  
class Linked_list:
    def __init__(self):
        self.head = None
        
        
    def transverse(self):
        if self.head is None:
            print("List has no Element")
            return
        
        else:
            n = self.head
            while n is not None:
                print(n.element)
                n = n.next
                
                
    #Insert at start
    
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert element at end 

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node
        
        
     #insert element after the defined element 
    
    def insert_after_element(self,x, data):
        n = self.head
        print(n.next)
        while n is not None:
            if n.element == x:
                break
            n = n.ref
            
        if n is None:
            print("element not in the List")
            
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
            
            
            
    def insert_before_element(self,x, data):
        n = self.head
        print(n.next)
        if x == n.element :
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        
        n = self.start_node
        print(n.next)
        while n.next is not None:
            if n.next.item == x:
                break
                
            n = n.next
        if n.next is None:
            print("item not in the list")
            
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node
          
        
    def delete(self,x):
        if self.head is not None:
            if self.head.element == x:
                self.head = self.head.next
                return
        n = self.head
        while (n is not None):
            if n.element == x:
                break
            prev = n
            n = n.next
    
        if n==None:
            return
        prev.next = n.next
        temp= None          
        
                
                
        
