"""
Stack Data Structure.
"""
class Stack():
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
     
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    
# mystack = Stack()
# mystack.push("A")  
# mystack.push("B") 
# mystack.push("C") 
# print(mystack.get_stack())  
# mystack.pop() 
# mystack.push("D") 
# mystack.push("E") 
# print(mystack.get_stack())  
# mystack.pop()  
# mystack.push("G") 

# print(mystack.get_stack())  