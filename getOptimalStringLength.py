#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getOptimalStringLength' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER countA
#  2. INTEGER countB
#  3. INTEGER maxA
#  4. INTEGER maxB
#

def getOptimalStringLength(countA, countB, maxA, maxB):
    # Write your code here
    if countB > countA:
        r = countB - maxB
        return r + countA
    if countA == countB:
        return countA + countB
        
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    countA = int(input().strip())

    countB = int(input().strip())

    maxA = int(input().strip())

    maxB = int(input().strip())

    result = getOptimalStringLength(countA, countB, maxA, maxB)

    #fptr.write(str(result) + '\n')

    #fptr.close()
