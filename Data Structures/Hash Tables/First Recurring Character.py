
#O(n)
def simple_frc(array):
    dictionary = dict()
    for item in array:
        if item in dictionary:
            return item
        else:
            dictionary[item] = True
    return None


array = [2,1,4,1,5,2,6]
print(simple_frc(array))

