# take 2 choices then one is A and other is B compare it, then if correct move on score +1 
# else stop the game and display the score
# while score changes by one make B our new A and different Thing turns B 
# while keeping in mind the previous A cant come again 
# both A and B shouldnt comeback into the list again
import random 
from dataset import data
import os


def picker(picked_list):
    # picks 2 dictornary from the data and checks if it is picked before
    # if it is picked then it re runs it and keeps going till we have our set for higher and lower
    while True:
        picked_dic= random.choice(data)
        if picked_dic["name"] not in picked_list:
            picked_list.append(picked_dic["name"])
            return picked_dic

def compare(pickA, pickB):
    # compares the if it is higher or lower 
    # returns 1 if correct else returns 0 
    while True:
        user_pick = input("Who has more followers A or B ?\n").lower().strip()
        if user_pick in ["a","b"]:
            if user_pick == "a" and pickA > pickB:
                return 1
            elif user_pick == "b" and pickA< pickB:
                return 1
            else:
                return 0
        else:
            print("Enter A or B, and Try again!")

def playgame():
    round_on = True
    score= 0
    picked_list= []
    A_dict = picker(picked_list)
    B_dict = picker(picked_list)
    while round_on:
        os.system("cls")
        print(f"Score: {score}")
        print("Choice A:"+A_dict["name"]+", "+ A_dict["description"]+" , from "+A_dict["country"] )
        print("VS")
        print("Choice B:"+B_dict["name"]+", "+ B_dict["description"]+" , from "+B_dict["country"] )
        choice= compare(A_dict["follower_count"],B_dict["follower_count"])
        if choice ==0:
            print(f"Your score was {score}")
            round_on= False
        else:
            score += 1
            A_dict= B_dict
            B_dict= picker(picked_list)
    if round_on == False:
        print("Do you want to play another round?")
        more_round = input("Enter Yes/Y to play, or enter any key to exit:\n").lower().strip()
        if more_round in ["yes","y"]:
            playgame()
        else:
            print("Thank you for playing!")

playgame()