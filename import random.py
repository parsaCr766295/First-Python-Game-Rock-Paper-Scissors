import random 
a=['sang', 'kagaz', 'ghychi']
computer=random.choice (a)
man=input("Enter a choice (sang, kagaz, ghychi): ")
if computer == "sang" and man =="ghychi":
    print("bkhti")
elif computer == "ghychi" and man =="sang":
    print("bordi")
elif computer == "kagaz" and man == "ghychi":
    print("bordi")
elif computer == "ghychi" and man == "kagaz":
    print("bkhti")
elif computer == "sang" and man == "kagaz":
    print("bordi")
elif computer == "kagaz" and  man == "sang":
    print("bkhti")
else:
    print("mosavi")
print(f"man {computer} entkhab karde bodam")
print(f"\nYou chose {man}, computer chose {computer}.\n")


# user_action = input("Enter a choice (rock, paper, scissors): ")
# possible_actions = ["rock", "paper", "scissors"]
# computer_action = random.choice(possible_actions)
# print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#
# if user_action == computer_action:
#     print(f"Both players selected {user_action}. It's a tie!")
# elif user_action == "rock":
#     if computer_action == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif user_action == "paper":
#     if computer_action == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif user_action == "scissors":
#     if computer_action == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")
import random
a=['sang', 'kagaz', 'ghychi']
computer=random.choice (a)
man=input("Enter a choice (sang, kagaz, ghychi): ")
if computer == "sang" and man =="ghychi":
    print("bkhti")
elif computer == "ghychi" and man =="sang":
    print("bordi")
elif computer == "kagaz" and man == "ghychi":
    print("bordi")
elif computer == "ghychi" and man == "kagaz":
    print("bkhti")
elif computer == "sang" and man == "kagaz":
    print("bordi")
elif computer == "kagaz" and  man == "sang":
    print("bkhti")
else:
    print("mosavi")
print(f"man {computer} entkhab karde bodam")
print(f"\nYou chose {man}, computer chose {computer}.\n")


# user_action = input("Enter a choice (rock, paper, scissors): ")
# possible_actions = ["rock", "paper", "scissors"]
# computer_action = random.choice(possible_actions)
# print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
#
# if user_action == computer_action:
#     print(f"Both players selected {user_action}. It's a tie!")
# elif user_action == "rock":
#     if computer_action == "scissors":
#         print("Rock smashes scissors! You win!")
#     else:
#         print("Paper covers rock! You lose.")
# elif user_action == "paper":
#     if computer_action == "rock":
#         print("Paper covers rock! You win!")
#     else:
#         print("Scissors cuts paper! You lose.")
# elif user_action == "scissors":
#     if computer_action == "paper":
#         print("Scissors cuts paper! You win!")
#     else:
#         print("Rock smashes scissors! You lose.")
