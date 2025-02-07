rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose=int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("computer chose:")
comp=random.choice([rock,paper,scissors])
print(comp)
if choose==0:
    if comp==rock:
        print("draw")
    elif comp==paper:
        print("you lose")
    else:
        print("you win")
if choose==1:
    if comp==rock:
        print("you win")
    elif comp==paper:
        print("draw")
    else:
        print("you loose")
if choose==2:
    if comp==rock:
        print("you loose")
    elif comp==paper:
        print("you win")
    else:
        print("draw")