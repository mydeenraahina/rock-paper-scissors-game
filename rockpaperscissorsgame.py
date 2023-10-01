import random
list=["rock","paper","scissors"]
x=random.choice(list)
def play():
    print("Loading...")
    choice1=input("[rock,paper,scissors]\nchoose any one of the following to play the game :")
    print("your choice :",choice1)
    print("computer choice :",x)
    if choice1=="rock" and x=="scissors":
        print("u won the game")
    elif choice1=="rock" and x=="paper":
         print("computer won the game")
    elif choice1=="rock" and x=="rock":
       print("u tied")
    if choice1=="paper" and x=="scissors":
         print("computer won the game")
    elif choice1=="paper" and x=="stone":
         print("u won the game")
    elif choice1=="paper" and x=="paper":
         print("u tied")
    if choice1=="scissors" and x=="paper":
         print("u won the game")
    elif choice1=="scissors" and x=="rock":
         print("computer won the game")
    elif choice1=="scissors" and x=="scissors":
          print("u tied")
print("welcome to rock,paper,scissors game")
choice=input("Do yoy want to paly the game :")
if choice=="yes":
    play()
else:
    print("exit")
while True:
    choice2=input("do you continue this game :")
    if choice2=="yes":
        play()
    else:
       print("exit")
       break

