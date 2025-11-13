import random
choices=["stone","paper","scissors"]
your_choice=input("enter your choice(stone/paper/scissors):")
computer_choice=random.choice(choices)
print("you choice:",your_choice)
print("computer choice:",computer_choice)
if your_choice==computer_choice:
    print("Result:it is a draw")
elif(your_choice=="stone" and computer_choice=="scissors")or (your_choice=="paper" and computer_choice=="stone")or (your_choice=="scissors" and computer_choice=="paper"):
    print("Result:user wins")
elif(your_choice in choices):
    print("Result:computer wins")
else:
    print("play again")