from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
def caeser(txt,shifting,which_direction):
  new_txt=""
  if(which_direction=="decode"):
        shifting*=-1
  for i in txt:
    if i in alphabet:
      indexOfLetter=alphabet.index(i)
      new_txt+=alphabet[(indexOfLetter+shifting)%len(alphabet)]
    else:
      new_txt+=i
  print(f"The {which_direction}d text is {new_txt}")

while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
    result=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(result=="no"):
       print("GoodBye")
       break






    