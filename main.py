import random
import os
import time
# import ai
# import house

available_players = ["player", "ai"]
current_turn = ""
turn_num = 0

#card_suits = [" of Hearts", " of Diamonds", " of Clovers", " of Spades"]
card_numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Queen", "King"]

player_cards = []
ai_cards = []

difficulty = ""

# total number in hand should have an algorithmic risk association to allow ai to "think"/take risks
# players total number in hand must also be evaluated to determine the risk/risk tolerance

player_hand_total = 0
ai_hand_total = 0

player_money = 500
ai_money = 500

player_bet = 0
ai_bet = 0
risk_bet = 0

game_running = True
determined_risk = False

def main():
    #difficulty = input("What difficulty do you want to play? (E/M/H): ")
    
    current_turn = random.choice(available_players)

    house(ai_cards, ai_hand_total, "ai")
    house(player_cards, player_hand_total, "ai")

    os.system("CLS")

    while game_running:
        if current_turn == "player":
            player()
        elif current_turn == "ai":
            ai()
        
        os.system("CLS")
        
        #house()

        if current_turn == "player":    current_turn = "ai"
        elif current_turn == "ai":      current_turn = "player"
        else: current_turn == "player"

        print("TURN IS NOW " + current_turn + ".\n")
        os.system("TIMEOUT 5")

def house(cards, hand_total, user):
    global player_cards
    global ai_cards
    global player_money

    # for x in range(2):
    #     card_to_give = random.choice(card_numbers)
    #     player_cards.append(card_to_give)
    #     card_to_give = random.choice(card_numbers)
    #     ai_cards.append(card_to_give)
    
    for x in range(2):
        card_to_give = random.choice(card_numbers)
        cards.append(card_to_give)

    check_total(cards, hand_total, user)
    
    if user == "player":
        player_bet = int(input("Enter a bet (You have $" + str(player_money) + "): $"))
        player_money -= player_bet
        print("You are betting $" + str(player_bet) + ". Your new total is $" + str(player_money) + ".")
        os.system("PAUSE")
    if user == "ai":
        pass

def player():
    os.system("CLS")

    # evaluate hand_total
    # for x in range(len(player_cards)):
    #     if player_cards[x] == "Ace": # if adding the regular ace value (11) will result in a bust, add 1 instead.
    #         if player_hand_total + 11 > 21:
    #             player_hand_total + 1
    #         else:
    #             player_hand_total + 11
    #     if player_cards[x] == "Queen":
    #         player_hand_total + 10
    #     if player_cards[x] == "King":
    #         player_hand_total + 10

    print("Your current cards: (" + str(check_total()) + "): ")
    for x in range(len(player_cards)):
        print(player_cards[x], end=" ")
        

    print("\nAI's current cards: (" + str(check_total()) + "): ")
    for x in range(len(ai_cards)):
        print(ai_cards[x], end=" ")

    choice = input("\n\n(S)tand | (H)it | (D)ouble down\n")

    if choice == "S": pass #stand("player")
    elif choice == "H": hit(player_cards, player_hand_total, "player")
    elif choice == "D": double_down(player_cards, player_hand_total, "player")

def ai(): # needs to determine risk and have risk tolerance factor to intelligently make a decision
    os.system("CLS")

    global risk_bet

    risk = 0
    risk_tolerance = 0 # percent chance to take a risk ( CHANGE THIS TO AN ACTUAL ALGORITHM )
    
    if not determined_risk:
        if difficulty.lower() == "e":       risk_tolerance = 65 # easy difficulty
        elif difficulty.lower() == "m":     risk_tolerance = 40 # medium difficulty
        elif difficulty.lower() == "h":     risk_tolerance = 15 # hard difficulty
        else:                               risk_tolerance = 50 # default difficulty


    if ai_hand_total + 6 > 21:
        stand(ai_cards, ai_hand_total, "ai")
    elif ai_hand_total + 6 < 22:
        random_roll = random.randint(1, 10)
        if random_roll <= 5:
            hit(ai_cards, ai_hand_total, "ai")
        else:
            double_down(ai_cards, ai_hand_total, "ai")
    else:
        stand(ai_cards, ai_hand_total, "ai")

def determine_risk():
    determined_risk = True

    global risk_bet

    if difficulty == 65:
        risk_bet = random.randint(4, 5)
    if difficulty == 40 or difficulty == 50 or difficulty == 15:
        risk_bet = random.randint(5, 6)

# functions with actions to play vvv #

def stand(cards, hand_total, user):
    os.system("CLS")

    print(user + " is going to stand with " + str(hand_total) + " total in hand.")
    check_total(cards, hand_total, user)

    os.system("PAUSE")
    os.system("CLS")

def hit(cards, hand_total, user):
    os.system("CLS")
    
    print(user + " is going to hit with " + str(hand_total) + " total in hand.")

    card_to_give = random.choice(card_numbers)
    cards.append(card_to_give)

    for x in range(len(cards)):
        print(cards[x], end=" ")
    print("\n")
    
    check_total(cards, hand_total, user)

def double_down(cards, hand_total, user):
    os.system("CLS")
    
    print(user + " is going to hit with " + str(hand_total) + " total in hand.")

    if player_bet * 2 <= player_money:
        card_to_give = random.choice(card_numbers)
        cards.append(card_to_give)

        for x in range(len(cards)):
            print(cards[x], end=" ")
        print("\n")

        check_total(cards, hand_total, user)
    else:
        print("You do not have enough money to double-down.\n")
        os.system("PAUSE")

def check_total(cards, hand_total, user):
    os.system("CLS")
    global player_hand_total
    global ai_hand_total

    print("hand total at start of function is " + str(hand_total))
    os.system("PAUSE")
    
    for x in range(len(cards)):
        if cards[x] == "Ace": # if adding the regular ace value (11) will result in a bust, add 1 instead.
            if hand_total + 11 > 21:
                hand_total += 1
            else:
                hand_total += 11
        elif cards[x] == "Queen":
            hand_total += 10
        elif cards[x] == "King":
            hand_total += 10

        elif cards[x] != "Ace" or cards[x] != "Queen" or cards[x] != "King":
            hand_total += int(cards[x])

    if hand_total > 21:
        print(user + " has bust.\n")
        available_players.remove(user)
        os.system("TIMEOUT 5")
    
    print(str(hand_total) + " current hand total")

    if user == "player":
        hand_total +  player_hand_total
    if user == "ai":
        hand_total + ai_hand_total
    
    # print(player_hand_total)
    # print(ai_hand_total)

    return hand_total
    
    os.system("PAUSE")

main()