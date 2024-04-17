class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):       
        self.root = None

    # def contains(self,value):
    def insert(self,value):
        new_node = Node(value)
        
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True: # temp is not None:
            if temp.value == value:
                return False
            
            if temp.value > value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right    
                
                
mytree= BinarySearchTree()
mytree.insert(2)
mytree.insert(1)
mytree.insert(4)
mytree.insert(5)    
mytree.insert(2)
mytree.insert(3)  

print(mytree.root.value)  
print(mytree.root.left.value)          
print(mytree.root.right.value)          
print(mytree.root.right.left.value)          
       
            
        
#create a new node
#if root ==None -> root = newnode
#temp = root
#while loop
#  if new node == temp  return False
# if <  left  else > right 
# if None, insert new node, else move next

