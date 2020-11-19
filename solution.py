#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    
    arr_list = dict(enumerate(arr,1))
    list_of_arr = {v:k for k,v in arr_list.items()}
    count = 0
    for i in arr_list:
        value = arr_list[i]
        if value != i:
            stored_value = list_of_arr[i]
            arr_list[stored_value] = value
            list_of_arr[value] = stored_value
            count+=1
    return count
        
def sort(arr, times):
    """
    first try with a recursive function
    """
    swaped = False
   
    for i in range(len(arr)):
        if i+1 != arr[i]:
            first_to_swap = arr[i]
            first_index = i
            swaped = True
            break
    
    for i in range(len(arr)):
        if swaped:
            if first_to_swap == i+1:
                second_to_swap = arr[i]
                second_index = i
                break
    
    if swaped:
        arr[second_index] = first_to_swap
        arr[first_index] = second_to_swap
        times += 1
        times = sort(arr, times)
    
    return times
 
if __name__ == '__main__': 
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    sys.setrecursionlimit(100000)

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
