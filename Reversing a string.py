def reverse(str):
    if ( len(str)<2):
        return str

    newstr = []
    for i in range(len(str)-1,-1,-1):
        newstr.append(str[i])
    return ''.join(newstr)
    # str[::-1]



reverse('abc')   