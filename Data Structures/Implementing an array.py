class Array:
    def __init__(self):
        self.length =0
        self.data ={}
    def __str__(self):
        return str(self.__dict__)
    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length +=1
        return self.length

    def pop(self):

        lastitem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -=1
        return lastitem
    
    def delete(self,index):
        item = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1] #The last element which remains two times in the array is deleted
        self.length -=1
        return item


arr = Array()

arr.get(0)
arr.push('1')
arr.pop()
arr.delete(2)
print(arr)
    
    