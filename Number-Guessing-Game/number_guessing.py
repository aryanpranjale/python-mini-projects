import random
def difficulty_picker():
    diff_list= ["1","2","3","easy","medium","hard"]
    while True:
        print('''Choose the difficulty to play:
        1. Easy
        2. Medium
        3. Hard''')
        dif_level= input("Enter the number or" \
        " the difficulty you want to play: \n ").strip().lower()
        if dif_level in diff_list:
            if dif_level in ["easy","1"]:
                return "easy"
            elif dif_level in ["medium","2"]:
                return "medium"
            else:
                return "hard"
        else:
            print("Try again putting" \
            "\n 1 for easy" \
            "\n 2 for medium" \
            "\n 3 for hard")
def number_picker(difficulty):
    #pick a number from given difficulty
    if difficulty =="easy":
        num_range = 10
        
    elif difficulty == "medium":
        num_range = 100
        
    else:
        num_range = 1000
        
    random_num= random.randint(1,num_range)
    return random_num, num_range

def play_game():
    while True:
        dif = difficulty_picker()
        ran=number_picker(dif)
        (ran_num,number_range) = ran
        on_going_round = True
        guessed_numbers= []
        tries = 0
        while on_going_round :
            print(f"The number is in the range of 1 to {number_range}")
            
            try:
                player_guess = int(input("Whats your guess? \n")) 
                if player_guess not in guessed_numbers:
                    tries += 1
                    if player_guess < ran_num:
                        print(f"The number is higher then {player_guess}")
                        guessed_numbers.append(player_guess)
                        print(f"{player_guess}<")
                    elif player_guess > int(ran_num):
                        print(f"The number is lower than {player_guess}")
                        guessed_numbers.append(player_guess)
                        print(f"{player_guess}>")
    
                    else:
                        print(f"Good job you guessed the number {ran_num} in {tries} tries")
                        on_going_round = False
                else:
                    print("Enter a different one!")
                    
                    
            except ValueError:
                print("Enter a number")
        print("Do you want to play another round?")
        another_round= input("Enter Yes/Y to play, and any other key to exit:\n").strip().lower()
        if another_round not in ["yes","y"]:
            print("Thank you for play! See you again!")
            break
        else:
            on_going_round = True


play_game()