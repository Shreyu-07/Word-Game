import getpass as gp 
import random
import time
print("Welcome to the game of gussing....")
print("It is the only for 2 people, whon should tpe the word and another should guss")
wrName = input(":: Entet the Typer name : ").strip()
gsName = input(":: Entet the gusser name : ").strip()

time.sleep(2)
while True:
    whoAreYou = input("If u are Typer say ' yes ' or else say 'no' ").lower().strip()
    if whoAreYou == "yes":
        while True :
            word = gp.getpass("Enter the word : ").lower().strip()
            li = []
            for i in word :
                li.append(i)

            random.shuffle(li)
            join = "".join(map(str,li))
            print(join)

            time.sleep(3)

            ansgss = input("Enter you guss : ")

            if ansgss == word :
                print("You the right")
                break
            else:
                print("Better luck next time")
                break
    else:
        print("Only Typer should use for first ... !")
    continuOrNO = input("Do u want to continew : (Yes/NO)  ::  ").lower().strip()
    if continuOrNO != "yes" :
        break