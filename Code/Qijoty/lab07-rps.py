import random
i=0
while i < 3:
    
    print("\n\nROCK PAPER SCISSORS TOURNAMENT\n")
    print("Get ReAdy to RUMBLEEEEEE\n\n")
    
    print("FIGHT\n")
    
    choices = ["rock", "paper", "scissors"]
    user = input(f"Choose one {choices} \n") #\n is for a new line
    
  computer_score = 0
  human_score = 0
    #\t is tab if __name__ == '__main__':

while True:
    print(f"Your score {user_score}")
    print(f"The Computer's score {computer_score}")
    win = (f"Wow, you're a winner!{user_wins}") 
    lose = (f"Muahaha, you're a loser {user_lose}")
    tie = (f"Crapper, a tie!! {user_tie}")
    


    computer = random.choice(choices)

    print()
    if user == computer:
        print(tie)
    elif user == "rock" and computer == "scissors":
        print("You chose rock and computer chose scissors")
        user_wins += 1
        print(win)
    elif user == "rock" and computer == "paper":
        print("You chose rock and computer chose paper")
        user_lose += 1
        print(lose)
    elif user == "scissors" and computer == "rock":
        print("You chose scissors and computer chose rock")
        user_lose += 1
        print(lose)
    elif user == "scissors" and computer == "paper":
        print("You chose scissors and computer chose paper")
        user_lose += 1
        print(win)
    elif user == "paper" and computer == "scissors":
        print("You chose paper and computer chose scissors")
        user_lose += 1
        print(lose)
    elif user == "paper" and computer == "rock":
        print("You chose paper and computer chose rock")
        user_lose += 1
        print(win)

    
    i += 1
    
