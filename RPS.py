import random
list=["rock","paper","scissor"]
mymark=0
computermark=0
n=int(input("Please let me know how many times you want to play \n" ))
for i in range(n):
    player=input("rock,paper,scissor? \n")
    computer=random.choice(list)
    if player==computer:
        print("Tie!")
    elif player=="rock":
        if computer=="paper":
           print("You lose!Computer covers player\n")
           computermark=computermark+1
        else:
            print("You win! player smashes computer \n")
            mymark=mymark+1
    elif player=="paper":
        if computer=="scissor":
            print("You lose! computer cuts player\n")
            computermark=computermark+1
        else:
            print("You win! player covers computer \n")
            mymark=mymark+1
    elif player=="scissor":
        if computer=="rock":
            print("You lose! computer smashes player \n")
            computermark=computermark+1
        else:
            print("You win! player cuts computer \n")
            mymark=mymark+1
    else:
        print("No valid reply! please check your spelling \n")
if mymark>computermark:
    print("PLAYER WINS!")
if mymark<computermark:
    print("COMPUTER WINS")
if mymark==computermark:
    print("Game ends in darw")
    
    
    
