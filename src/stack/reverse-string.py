from  stack import Stack

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_string=""
    while not stack.is_empty():
        rev_string += stack.pop()       
        
    return rev_string
    
stack= Stack()
print(reverse_string(stack,"tHIS IS A S TEST TSINGNNN"))    