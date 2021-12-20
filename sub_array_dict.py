# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:17:47 2021

@author: manik
"""
import os, datetime

arr= [1,2,3,4,1,9,12,9,8,7,8,9,10,9,16,1,2,3,4,5,6,7,8,9,10]

def sub_array(arr,n,start=0):
    sub_array_dict={}
    for i in range(start, len(arr)-1):
        if arr[i] > arr[i+1]:
            length= (i+1) - start
            sub_array_dict[length] = arr[start:i+1]
            start= i+1
        elif i+1 == len(arr)-1:
            length= len(arr) - start
            sub_array_dict[length] = arr[start:i+2]
            start= i+1
                
    key_list= sorted(list(sub_array_dict.keys()))
    sorted_list= key_list[::-1]
    print(sub_array_dict[sorted_list[n-1]])
    
arr1= [1,2,3,1,2,1,2,3,4,5,6,4,5,6,5,4,3,2,1]

sub_array(arr1,2) 


    