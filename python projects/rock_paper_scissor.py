import random

choice_list = ['ROCK', 'PAPER', 'SCISSOR']

user_choice = input("Enter Your Choice (ROCK, PAPER, SCISSOR): ").upper()
computer_choice = random.choice(choice_list)

print(f"User choice = {user_choice}")
print(f"Computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Tie")

elif user_choice == 'ROCK':
    if computer_choice == 'SCISSOR':
        print("User wins")
    else:
        print("Computer wins")

elif user_choice == 'PAPER':
    if computer_choice == 'ROCK':
        print("User wins")
    else:
        print("Computer wins")

elif user_choice == 'SCISSOR':
    if computer_choice == 'PAPER':
        print("User wins")
    else:
        print("Computer wins")

else:
    print("Invalid choice")
