# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:59:23 2023

@author: Loges
"""

from itertools import permutations

def numcreator(s, dct):
    num=0
    for j in s:
        num=(num*10)+dct[j]
    return num

s1='cross'#input("First word:").strip()
s2='roads'#input("Second word:").strip()
s3='danger'#input("Third word:").strip()

letters=list(set(s1+s2+s3))
digits=permutations(range(10),len(letters))
dct={}
for i in digits:
    for j in range(len(letters)):
        dct[letters[j]]=i[j]
    n1=numcreator(s1,dct)
    n2=numcreator(s2,dct)
    n3=numcreator(s3,dct)
    if(n1+n2==n3):
        print(dct)
