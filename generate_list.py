def generateList(startvalue, endvalue):
    # Write your code here
    list1 = list(range(startvalue,endvalue+1))
    print(list1)
    print(list1[:3])
    list2 = list1[::-1]
    print(list2)
    print(list2[0:5])
    print(list1[::4])
    print(list2[::2])

if __name__ == '__main__':
    startvalue = int(input().strip())

    endvalue = int(input().strip())

    generateList(startvalue, endvalue)
