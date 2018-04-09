import random


#Rock, Paper, Scissors Game: variables & lists
human = ""
computer = ""
choices = ["Rock", "Paper", "Scissors"]
play_again = input("Want to play Rock, Paper, Scissors? ")
human_score = 0
computer_score = 0


#Game function
def rps_game ():
    global human_score
    global computer_score

    
    #1st part of the function to get computer and human choices
    computer = random.choice(choices)
    human = input("Please select 'r' for Rock, 'p' for Paper, or 's' for" \
    " Scissors:")
    if human == "r":
        print("Player chooses: Rock")
    elif human == "s":
        print("Player chooses: Scissors")
    elif human == "p":
        print("Player chooses: Paper")
    print("Computer chooses:",computer)


    #2nd part of function to determine who wins and to assign score
    if computer == "Rock" and human == "s":
        print("Computer wins!")
        computer_score += 1
    elif computer == "Scissors" and human == "p":
        print("Computer wins!")
        computer_score += 1
    elif computer == "Paper" and human == "r":
        print("Computer wins!")
        computer_score += 1
    elif human == "r" and computer == "Scissors":
        print("Player wins!")
        human_score += 1
    elif human == "s" and computer == "Paper":
        print("Player wins!")
        human_score += 1
    elif human == "p" and computer == "Rock":
        print("Player wins!")
        human_score += 1
    else:
        print("Draw!")

        
#While loop to keep looping/playing the game and building scores
while(1):        
    rps_game()
    print("Current score is: Player- ", human_score, " Computer- ", computer_score)
 


