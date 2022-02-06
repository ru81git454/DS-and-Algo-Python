# 10 -> 20->30
from platform import node


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 0
    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()

    # O(1)
    def append(self,data):
        node = Node(data)
        if self.head ==None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
        return self.print_list()
    # O(1)
    def prepend(self,data):
        node = Node(data)
        if self.head ==None:
            self.head = node
            self.tail = node
            self.length = 1
        else:
            current_node = self.head
            node.next = current_node
            self.head = node
            self.length += 1
        return self.print_list()
    # worst o(n)
    def insert(self,position, data):
        if position > self.length:
            return 
        if position == 0:
            self.prepend(data)
        elif position == self.length -1:
            self.append(data)
        else:
            node = Node(data)
            current_node = self.head

            for i in range(position-1):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node
            self.length +=1
            return self.print_list()



myLinkedList = LinkedList(10)
# 10
myLinkedList.print_list()

myLinkedList.append(20)
# 10 -> 20
myLinkedList.prepend(30)
# 30 -> 10 ->20 
myLinkedList.insert(2,5)
# 30 -> 10 -> 5 -> 20
myLinkedList.insert(0,5)