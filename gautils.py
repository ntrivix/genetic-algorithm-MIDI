# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:28:16 2017

@author: Nikol
"""

def binarisation(arr,n):
    bin = []
    for num in arr:
        a = num
        oaz = []
        for j in range(0,n):
            oaz.append(a % 2)
            a = int(a // 2)
        for j in range (n-1,-1,-1):
            bin.append(oaz[j])
    return bin

def unbinarisation(arr):
    res = 0
    val = 1
    for i in reversed(range(len(arr))):
        if (arr[i] == 1):
            res += val
        val *= 2
    return res