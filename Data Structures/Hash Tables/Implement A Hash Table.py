#80. Exercise: Implement A Hash Table
class HashTable:
    def __init__(self,size):
        self.size = size
        self.data = [None]* self.size
    def __str__(self):
        return str(self.__dict__)
    def _hash(self,key):
        hash = 0
        for i in range(len(key)):
            hash = (hash+ ord(key[i])*i) % self.size
        return hash

    def get(self,key): #Function to return the value of the key entered by the user
        hash = self._hash(key) #Hash value of the key is calculated by passsing the key to the _hash function
        if self.data[hash]: #Multiple items may exist in the position of the hash value returned by the hash function, so we have to chceck all of them
            for i in range(len(self.data[hash])): #We loop over the entire list of lists that may be present in the 'hash' position of the data array
                if self.data[hash][i][0] == key: #For every list in the list of lists(extracted by 'i'), we match the first element of the list with the given key
                    return self.data[hash][i][1] #If we get a match, we return the second element of that list, which is the value
        return None #If we don't find the key, we return None
    def set(self, key, value): #Function to insert a new key, value pair
            hash = self._hash(key) #Hash value of the key is calculated using the _hash function
            if not self.data[hash]: #If the 'hash' position of the data array is empty, we insert the key, value pair as a list
                self.data[hash] = [[key,value]]
            else: #If the 'hash' position is not empty, implying a collision, we simply append the list of key,value pair to the lists already present
                self.data[hash].append([key, value])
            print(self.data)
    def keys(self):
        keys_array = []
        for i in range(len(self.size)):
            if self.data[i]:
                if len(self.data[i])>1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
            else:
                keys_array.append(self.data[i][0][0])
    def values(self):
        values_array = []
        for i in range(len(self.size)):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])


new_hash = HashTable(2)
print(new_hash)
new_hash.set('one',1)
new_hash.set('two',2)
new_hash.set('three',3)
new_hash.set('four',4)
