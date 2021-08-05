#!/bin/python3

import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    # Write your code here
    temp=[]
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in s:
        if i in alpha:
            temp.append(alpha[alpha.index(i)+k] if alpha.index(i)+k<25 else caesarCipher(i,k-26))
        elif i.isupper():
            temp.append(alpha[alpha.index(i.lower())+k].upper() if alpha.index(i.lower())+k<25 else caesarCipher(i,k-26).upper())
        else:
            temp.append(i)
    return ''.join(temp)
                             
if __name__ == '__main__':
    
    n = int(input("Enter the length of the string"))

    s = input("Enter the uncrypted string")

    k = int(input("Enter the no. of letter to rotate the alphabet"))

    result = caesarCipher(s, k)

    print("The encrypted string is",result)
