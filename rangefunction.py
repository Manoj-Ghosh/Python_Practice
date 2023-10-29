def rangefunction(startvalue, endvalue, stepvalue):
    # Write your code here
    for i in range(startvalue,endvalue,stepvalue):
        print(i*i,end = "\t")


if __name__ == '__main__':

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    rangefunction(x, y, z)