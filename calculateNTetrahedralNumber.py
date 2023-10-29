import os
def calculateNTetrahedralNumber(startvalue, endvalue):
    # Write your code here
    list1 = list()
    i = startvalue
    while i<= endvalue:
        num = (i*(i+1)*(i+2)/6)
        list1.append(int(num))
        i = i + 1
    return list1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    startvalue = int(input().strip())

    endvalue = int(input().strip())

    result = calculateNTetrahedralNumber(startvalue, endvalue)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
