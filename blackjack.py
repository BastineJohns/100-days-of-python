import random



def total_calculator(cards):
    total = sum(cards)
    if total>21 and 11 in cards:
        cards[cards.index[11]] = 1
        total = sum(cards)
    return total


         
def main(): 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    decision = input("Do you want to play black jack?'YES' OR 'NO'").lower()
    

    while decision == 'yes':
        user_set = []
        dealer_set = []

        for picks in range(2):
            user_card = random.choice(cards)
            dealer_card = random.choice(cards)
            user_set.append(user_card)
            dealer_set.append(dealer_card)
        print(f"YOUR CARDS ARE {user_set}")
        print(f"COMPUTER CARD IS {dealer_set[0]}")
        user_score = total_calculator(user_set)
        dealer_score = total_calculator(dealer_set)
        if dealer_score == 21:
            print("DEALER'S HAND IS BLACKJACK, YOU LOSE!")
            print(f"DEALER'S HAND IS{dealer_score}")
            break
        elif user_score == 21:
            print("YOU HAVE BLACKJACK, YOU WIN!")
            break
        else:
            decision2 = input("Do you want to deal with another card?'YES' OR 'NO'").lower()
            while decision2 == 'yes':
                    user_card = random.choice(cards)
                    print(f"YOUR CARD IS {user_card}")
                    user_set.append(user_card)
                    user_score = total_calculator(user_set)
                    if user_score > 21:
                        print("YOU HAVE BUSTED, YOU LOSE!")
                        break
                    elif user_score == 21:
                        print("YOU HAVE BLACKJACK, YOU WIN!")
                        break
                    else:
                        decision2 = input("Do you want to deal with another card?'YES' OR 'NO'").lower()
            while dealer_score < 17:
                dealer_card = random.choice(cards)
                dealer_set.append(dealer_card)
                dealer_score = total_calculator(dealer_set)
            print(f"DEALER'S CARDS ARE {dealer_set}")
            if user_score > dealer_score: 
                 print("YOU WIN!")
            else:      
                print("YOU HAVE BUSTED, YOU LOSE!")
        decision = input("Do you want to play black jack?'YES' OR 'NO'").lower()        
                                
main()