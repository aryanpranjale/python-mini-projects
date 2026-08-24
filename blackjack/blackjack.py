import random

#card_deck=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
number_cards=[str(i) for i in range(2,11)]
Ace=["A"]
face_cards=["J","Q","K"]
card_deck = Ace + number_cards + face_cards

def user_play():
    # give the player the cards and shows them
    player_cards= []
    for _ in range (2):
        player_cards.append(random.choice(card_deck))
    print(player_cards)
    return player_cards
def dealer_play():
    # give the dealer his cards and shows only one of them
    dealer_cards=[]
    for _ in range (2):
        dealer_cards.append(random.choice(card_deck))
    print(dealer_cards[0])
    return dealer_cards

def start_or_not():
    # 1 will start the game, 0 will end
    print("Do you want to play a round of blackjack?")
    player_wish= input("Enter Yes/Y to play, Else enter any key to exit:\n").strip().lower()
    if player_wish in ["yes","y"]:
        print("Get ready to play")
        return 1
    else:
        print("See you again!")
        return 0
def hit(hand):
    hand.append(random.choice(card_deck))
def total_value(hand):
    # calculates the total value and returns it to the code
    total = 0 
    ace_counter = 0
    for i in hand:
        try:
            card_facevalue = int(i)
            total += card_facevalue
        except ValueError:
            if i in face_cards:
                total += 10
            elif i in Ace:
                total += 11
                ace_counter += 1
    while total > 21 and ace_counter >0:
        total -= 10
        ace_counter -=1
    return total         
    
def play_game():
     while True:
        start= start_or_not()
        user_total= 0
        dealer_total = 0
        if start==1 :
            user_hand= user_play()
            dealer_hand= dealer_play()
            player_bust = False
            while not player_bust :
                    print("Hit or Stand")
                    hit_or_stand= input("Enter Hit/H to hit and Stand/S to stand:\n").strip().lower()
                    if hit_or_stand in ["hit","h"]:
                        hit(user_hand)
                        print(user_hand)
                        if total_value(user_hand) > 21:
                            print("BUST")
                            print("You lose!")
                            player_bust = True
                    elif hit_or_stand in ["stand","s"]:
                        break   
                    else:
                        print("Try again! enter h for hit and s for stand")
            if not player_bust:
                user_total= total_value(user_hand)
                print(dealer_hand)
                dealer_total = total_value(dealer_hand)
                while dealer_total < 17:
                    hit(dealer_hand)
                    dealer_total = total_value(dealer_hand)
                print(dealer_hand) 
                if dealer_total>21 :
                    print("Dealer bust, You win!")
                else:
                    print(f"Your score was: {user_total}")
                    print(f"Dealers' score was : {dealer_total}")
                    if user_total> dealer_total:
                        print("You win!")
                    elif user_total < dealer_total:
                        print("Dealer wins!")
                    else: 
                        print("Draw")
        else:
            break    


play_game()