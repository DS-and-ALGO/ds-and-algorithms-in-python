from stack import Stack
#import math

def convert_int_to_bin(number):
    if number == 0:
      return 0
    
    s= Stack()   
    while number> 0:
        remainder= number%2
        print(remainder)
        s.push(remainder)
        number=number//2
        print(number)
        
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num   

print(convert_int_to_bin(123))
    