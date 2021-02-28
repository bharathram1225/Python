''' here is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .'''


import math
import os
import random
import re
import sys
from collections import Counter 

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    s=0
    for val in Counter(ar).values():
        print(val, end="  ")
        s+=val//2
    return s
      


if __name__ == '__main__':
   

    n = 10
    ar = [1,1,1,3,3,3,4,4,7,6,5,3]
    abc = sockMerchant(n,ar)
    print(abc)
