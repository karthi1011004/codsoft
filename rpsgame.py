import random

play_again = "yes"

print("Let's start to play!")
print("_______________________")
print("Rock Paper Scissor")
print("_______________________")

while play_again != "no":
    computer = ["rock", "paper", "scissor"]
    computer_choice = random.choice(computer)
    computer_score = 0
    user_score = 0

    for _ in range(3):
        user_input = input("Enter Your choice:").lower()

        if user_input == "paper" and computer_choice == "rock":
            user_score += 1
        elif user_input == "scissor" and computer_choice == "paper":
            user_score += 1
        elif user_input == "rock" and computer_choice == "scissor":
            user_score += 1

        elif user_input == "rock" and computer_choice == "paper":
            computer_score += 1
        elif user_input == "paper" and computer_choice == "scissor":
            computer_score += 1
        elif user_input == "scissor" and computer_choice == "rock":
            computer_score += 1

    if user_score > computer_score:
        print(f"Congratulations! You win the match, and your score is: {user_score}")
        print(f"Computer score is {computer_score}")
    elif computer_score > user_score:
        print(f"Oops! Computer wins the match, and its score is {computer_score}")
        print(f"Your score is {user_score}")
    elif user_score == computer_score:
        print("Match tied")

    play_again = input("Do you want to play again? yes/no: ").lower()
