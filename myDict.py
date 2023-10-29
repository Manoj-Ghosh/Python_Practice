def myDict(key1, value1, key2, value2, value3, key3):
    # Write your code here
    dict1 = {key1:value1}
    print(dict1)
    dict1[key2] = value2
    print(dict1)
    dict1[key1] = value3
    print(dict1)
    dict1.pop(key3)
    return dict1

if __name__ == '__main__':
    key1 = input()

    value1 = input()

    key2 = input()

    value2 = input()

    value3 = input()

    key3 = input()

    mydct = myDict(key1, value1, key2, value2, value3, key3)
    
    print(mydct if type(mydct) == dict else "Return a dictionary")
    