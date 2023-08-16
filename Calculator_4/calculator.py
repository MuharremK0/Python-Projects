from os import system
from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def power(n1,n2):
    return n1**n2


operations={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    "^" : power,
}
def calculator():
    print(logo)

    first_num=float(input("What's the first number?: "))
    for i in operations:
        print(i)
    while(True):
        choice=input("Pick an operation: ")
        second_num=float(input("What's the next number?: "))

        function=operations[choice]
        result=function(first_num,second_num)
        print(f"{first_num} {choice} {second_num} = {result}")

        continueing=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if(continueing=="y"):
            first_num=result
        elif(continueing=="n"):
            system("cls")
            calculator()

calculator()


