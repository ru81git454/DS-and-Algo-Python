class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class doubleLinkedList():
    def __init__(self,data):
        self.head = None
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
            node.previous = self.tail
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
            current_node.previous = node
            self.head = node
            self.length += 1
        return self.print_list()
    # worst o(n)
    def insert(self,position, data):
        if position > self.length:
            self.append(data) 
        if position == 0:
            self.prepend(data)
        elif position == self.length -1:
            self.append(data)
        else:
            node = Node(data)
            current_node = self.head

            for i in range(position-1): # find the node before target position
                current_node = current_node.next
            node.next = current_node.next
            node.previous = current_node
            current_node.next = node
            node.next.previous = current_node
            self.length +=1
            return self.print_list()
    def remove_by_index(self, position):
        if position > self.length:
            return 
        if position == 0:
            self.head = self.head.next  
            if self.head is None or self.head.next is None:
                self.head = self.tail 
            if self.head != None:
                self.head.previous = None
        else:
            current_node = self.head

            for i in range(position-1): # find the node before target position
                current_node = current_node.next

            current_node.next = current_node.next.next
        self.length -=1
        if current_node.next != None:
                current_node.next.previous = current_node

        if current_node.next is None:
            self.tail = current_node
        if self.head != None:
            self.head.previous = None
        return self.print_list()
    
    def remove_by_value(self, data):
        if self.head is None:
            return self.print_list()
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next
            if self.head ==None or self.head.next == None:
                self.tail = self.head
                self.length -= 1

        #fing the node before target value and the node should not be last node
        while current_node.next !=None and current_node.next.data!= data:
            current_node = current_node.next

        if current_node.next !=None :
            current_node.next = current_node.next.next
            if current_node.next==None:
                self.tail = current_node
            else:
                current_node.next.previous = current_node #Then we set the previous of the node next to the deleted node equal to the current node, so a two-way link is established
            self.length -= 1
        else: 
            print("Given value not found.")

        

        return self.print_list()



myLinkedList = doubleLinkedList(10)
# 10

myLinkedList.append(20)
# 10 -> 20
myLinkedList.prepend(30)
# 30 -> 10 ->20 
myLinkedList.insert(2,5)
# 30 -> 10 -> 5 -> 20
myLinkedList.insert(0,5)
# 5 -> 30 -> 10 -> 5 -> 20
myLinkedList.remove_by_index(2)

myLinkedList.remove_by_value(20)
