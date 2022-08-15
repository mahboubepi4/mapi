# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:36:16 2022

@author: Mahboobeh
Number guessing game
"""
import random
n = random.randrange(0, 10)
f = "no"
while f == "no":
    a = int(input("What's your guess?"))
    if a < n:
           print("Increase your guessing number")
    elif a > n:
           print("Decrease your guessing number")
    else:
           print("Good job")
           f = "yes"

print("Thank you for playing.")