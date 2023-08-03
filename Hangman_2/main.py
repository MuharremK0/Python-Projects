import random;
import hangman_words;
import hangman_art;

#IF YOU WANNA PLAY THIS GAME,PUT COMMENT LINE IN LINE 14.

stages = hangman_art.stages 
word_list = hangman_words.word_list

chosen_word = random.choice(word_list) # Computer's choice

#Testing code
print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.') 


printing=[] 
guessed_words=[]

for i in chosen_word:
  printing.append("_")

count=len(chosen_word) # How many letters are remained
life=7 # Our life


print(printing)

while(count>0):
  condition1=False # If we've already guessed the word before, we don't have to run other cod lines.
  guess = input("Guess a letter: ").lower()
  for letter in guessed_words:
    if(letter==guess):
      condition1=True
      print("You've already guessed")
  
  if(condition1 == False):
    guessed_words.append(guess)
    condition2=0 # If this condition is not equal to zero, the letter which we guessed is not in the real word.
    for i in range(len(chosen_word)):
      if(guess==chosen_word[i]):
        printing[i]=guess
        count-=1
        condition2+=1
    if (condition2 == 0):
      life-=1
  if(life != 7):
    print(stages[life])
  print(printing)
  if(life == 0):
    print(f"You lost, it should be {chosen_word}")
    count=-1
if(count == 0):
  print("You won")
      

