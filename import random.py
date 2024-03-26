import random

# Define the possible choices
choices = ['sang', 'kagaz', 'gychi']

# Let the computer make a choice
computer_choice = random.choice(choices)

# Get the user's choice
user_choice = input("Enter a choice (sang, kagaz, gychi): ").lower()

# Check if the user's choice is valid
if user_choice not in choices:
    print("Invalid choice. Please try again.")
else:
        # Determine the winner
    if computer_choice == user_choice:
        print("It's a tie!")
    elif (user_choice == 'sang' and computer_choice == 'gychi') or \
         (user_choice == 'gychi' and computer_choice == 'kagaz') or \
         (user_choice == 'kagaz' and computer_choice == 'sang'):
        print("You win!")
    else:
        print("You lose!")

    print(f"Computer chose {computer_choice}.")
    print(f"You chose {user_choice}.")
