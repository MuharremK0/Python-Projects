from game_data import data
import art
import random
from os import system

bool=True #Only first time
score=0

while(True):
    if(bool):
        rand_num1=random.randint(0,len(data)-1)
        bool=False
    rand_num2=random.randint(0,len(data)-1)
    while(data[rand_num1]['follower_count'] == data[rand_num2]['follower_count']):
         rand_num2=random.randint(0,len(data)-1)
    print(art.logo)
    if(score!=0):
        print(f"You're right.Your current score is {score}")
    print(print(f"Compare A: {data[rand_num1]['name']}, {data[rand_num1]['description']}, {data[rand_num1]['country']}"))
    print(art.vs)
    rand_num=random.randint(0,len(data)-1)
    print(f"Against B: {data[rand_num2]['name']}, {data[rand_num2]['description']}, {data[rand_num2]['country']}")
    chosen=input("Who has more followers? Type 'A' or 'B': ")
    if(data[rand_num1]['follower_count'] > data[rand_num2]['follower_count'] and chosen=="A"):
        score+=1
    elif(data[rand_num1]['follower_count'] < data[rand_num2]['follower_count'] and chosen=="B"):
        score+=1
    else:
        system("cls")
        print(art.logo)
        print(f"Sorry, that's wrong. Your Final score is {score}")
        break
    rand_num1=rand_num2
    system("cls")