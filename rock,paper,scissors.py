import random

while True:
    user_action=input("Enter a Choice (rock,paper,scissors): ")
    possible_actions=["rock","paper","scissors"]
    computer_action=random.choice(possible_actions)
    print("You chose:", user_action)
    print("Computer chose: ", computer_action)

    if user_action==computer_action:
        print("Both players selected {user_action}. It's a tie.")
    elif user_action.lower()=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    
    play_again=input("Play again? (yes/no)")
    if play_again.lower()=="no":
        print("Okay! See you next time.")
        break
    else:
        print("Well done! Let's start again.")