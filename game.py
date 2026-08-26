import random

def game():
    a=["r","p","s"]
    b=random.choice(a)
    c=input("Choose rock paper or scissors(r,p,s) :")
    if c not in "rps":
        print("Error")
    elif b==c:
        print("Tie")
    elif b=="r" and c=="p":
        print("YOU WON")
    elif b=="s" and c=="r":
        print("YOU WON")
    elif b=="p" and c=="s":
        print("YOU WON")
    else :
        print("YOU LOST")
    

game()