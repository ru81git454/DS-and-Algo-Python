# Stakcs LIFO 
# suck as browser has visit history, you eant to see the previous page 

# build queues in linkedlist, only need O(1) to change pointer
# because array has index associated with it, once we remove it, we need to shift the index over, it is O(n).


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        return self.top
    def push(self,value):
        newnode = Node(value)
        if self.length ==0:
            self.top = newnode
            self.bottom = newnode
            self.length =1
        else:
            tmp = self.top
            self.top = newnode
            newnode.next = tmp
            self.length +=1
    def pop(self):
        if self.top == None:
            print("Stack Empty")
        else:
            self.top = self.top.next
            self.length -=1
            if (self.length == 0):
                self.bottom =None
    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while(current_pointer!=None):
                print(current_pointer.data)
                current_pointer = current_pointer.next

my_stack = Stack()
print(my_stack.peek())
#None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
