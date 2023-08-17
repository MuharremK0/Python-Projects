import random
from os import system
from art import logo

#Take a card
def cardChecker(deck1,deck2):
    chosen1=random.choice(deck1)
    deck2.append(chosen1)
    deck1.remove(chosen1)
    return chosen1
def gameBlackJack():
    #printing logo
    print(logo)
    my_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    pc_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    my_current=[]
    pc_current=[]
    #Starting decks 
    for i in range(2):
        cardChecker(my_cards,my_current)
        cardChecker(pc_cards,pc_current)

    result=sum(my_current)
    resultOfPC=sum(pc_current)
    bool=True #Our ace control
    otherLoop=True #Blackjack control
    otherLoop2=True #Computer ace control
    #Blackjack
    if(sum(my_current) == 21 and len(my_current) == 2):
        otherLoop=False
        result=0
    if(sum(pc_current) == 21 and len(pc_current) == 2):
        otherLoop=False
        resultOfPC=0
    #If blackjack doesn't happen and sum of pc cards less than 17, pc must take cards.
    if(otherLoop):
        while(sum(pc_current) < 17):
            resultOfPC+=cardChecker(pc_cards,pc_current)
            if(resultOfPC > 21 and 11 in pc_current and otherLoop2):
                resultOfPC-=10
                otherLoop2=False
                pc_current.remove(11)
                pc_current.append(1)
    #Starting decks is printing
    print(f"Your deck: {my_current} total={result}\nDealers first card: [{pc_current[0]}]")
    #Continue or not
    while(otherLoop):
        if 11 in my_current and bool and result > 21:
            result-=10
            bool=False
            my_current.remove(11)
            my_current.append(1)
        if(result >= 21):
            break
        choice=input("If you wanna continue type 'y', otherwise type 'n: ")
        if(choice=="y"):
            result+=cardChecker(my_cards,my_current)
            if(result > 21 and 11 in my_current):
                result-=10
                my_current.remove(11)
                my_current.append(1)
            print(f"Your deck: {my_current} total={result}\nDealers first card: [{pc_current[0]}]")
        else:
            #print(f"Your deck: {my_current}\nDealers first card: [{pc_current[0]}]")
            break
    #Result part
    print("*****RESULT*****")
    print(f"Your deck: {my_current} total={result}")
    print(f"Dealers actual deck: {pc_current} total={resultOfPC}")

    if(result == resultOfPC):
        print(f"Draw! {result} - {result}")
    elif(result==0):
        print(f"Lucky blackjack, you won! {result} - {resultOfPC}")
    elif(resultOfPC==0):
        print(f"Sorry, computer has blackjack, dealer won! {resultOfPC} - {result}")
    elif(result > 21):
        print(f"Dealer won! {resultOfPC} - {result}")
    elif(resultOfPC > 21):
        print(f"You won! {result} - {resultOfPC}")
    elif(result > resultOfPC):
        print(f"You won! {result} - {resultOfPC}")
    else:
        print(f"Dealer won! {resultOfPC} - {result}")

while input("Do you want to play a game ? 'y' or 'n': ") == "y":
    system("cls")
    gameBlackJack()

