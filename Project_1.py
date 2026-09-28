import random
# 1 for rock
# 0 for scissor
# -1 for paper
computer = random.choice([0,1,-1])
yourturn = input("Enter your Choice: ")
youdict = {"r":1, "s":0, "p":-1}
reversedict = {1:"Rock", 0:"Scissor", -1:"Paper"}
you = youdict[yourturn]
print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]}")

if (computer == you):
    print("It's draw!")
else:
    if (computer==1 and you==0):
        print("You lose!")
    elif (computer==1 and you==-1):
        print("You win!")
    elif (computer==0 and you==1):
        print("You win!")
    elif (computer==0 and you==-1):
        print("You lose!")
    elif (computer==-1 and you==1):
        print("You lose!")
    elif (computer==-1 and you==0):
        print("You win!")
    else:
        print("Something went wrong!")
