
"""
Created on Wed Aug 17 13:37:02 2022


@author: Mahboobeh
"Rock", "Paper", "Scissors"
"""

import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = False
c_score = 0
p_score = 0
while True:
    player = input("rock, paper or scissors?")
    if player == computer:
        print("tie!")
    elif player == "rock":
        if computer == "paper":
            print("you lose!", computer, "covers", player)
            c_score += 1
        else:
            print("you win!", player, "smashes", computer)
            p_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("you lose!", computer, "cut", player)
            c_score += 1
        else:
            print("you win!", player, "covers", computer)
            p_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("you lose!", computer, "smashes", player)
            c_score += 1
        else:
            print("you win!", player, "cut", computer)
            p_score += 1
    elif player == "end":
        print("final scores:")
        print(f"computer:{c_score}")
        print(f"player:{p_score}")
        break
    
            














