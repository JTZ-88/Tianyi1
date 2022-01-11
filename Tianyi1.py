#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:08:25 2022

b) 104 times
c) ZZZZZ

@author: Tianyi Zhang     Year 12
"""

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]  
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]   
encrypted = input("Encypted Message:") 
value = []
result =[]
word =""

for i in range (0,len(encrypted)):
    value.append(encrypted[i])

for a in range(0,len(value)-1):
    if value[-1-a] > value[-2-a]:
        result.append(letters[numbers[letters.index(value[-1-a])] - numbers[letters.index(value[-2-a])]-1])
    else:
        result.append(letters[numbers[letters.index(value[-1-a])] +25 - numbers[letters.index(value[-2-a])]])
        
result.append(value[0])

for k in range (0,len(result)):
    word += result[-1-k]
print(word)




