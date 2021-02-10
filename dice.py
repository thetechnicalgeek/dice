#install random module

import random

print(" WELCOME TO ROLL THE DICE GAME!!!")
print("do you want to roll the dice ?  Type yes ...")
roll_dice=input(" type yes to start or no to quit : ")

while roll_dice:
    if roll_dice=='yes':
        print("dice is rolling ......")
        num=random.randint(1,6)
        print("the value of dice is : ", num)
        repeat=input(" do you want to roll again ? yes/no : ")
    else:
        print(" thanks ")
        break
            
    if repeat== 'yes':
        roll_dice=='yes'
    else:
        roll_dice=False
        print(" thanks for playing ")
