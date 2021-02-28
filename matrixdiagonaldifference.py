#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    a = []
    b = []
    l = len(arr[0])
    for i in range(l):
        print(arr[i][i])
        sum1 = arr[i][i] + sum1
    
    for i in range(l-1,-1,-1):
        print(arr[l-i-1][i])
        sum1= arr[l-1-i][i] + sum2


    return abs(sum1 - sum2)

if __name__ == '__main__':
    

    arr = [[2,3,4],[2,3,4],[3,6,8]]

    result = diagonalDifference(arr)
    print(result)
    
