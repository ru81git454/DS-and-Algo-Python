# Stakcs LIFO 
# suck as browser has visit history, you eant to see the previous page 

# build queues in linkedlist, only need O(1) to change pointer
# because array has index associated with it, once we remove it, we need to shift the index over, it is O(n).
from hashlib import new


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.array =[]
    def peek(self):
        return self.array[len(self.array) - 1]
    def push(self,value):
        self.array.append(value)
    def pop(self):
        if self.top == None:
            print("Stack Empty")
        else:
            self.array.pop()
    def print_stack(self):
        for i in range(len(self.array)-1, -1, -1):
            print(self.array[i])

my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
