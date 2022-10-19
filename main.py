from random import randrange

choices = ["Rock","Paper","Scissors"]


def playGame(playerChoice, computerChoice):
       
    if computerChoice == playerChoice:
      return "It's a tie!"
    elif computerChoice == "Rock":
      if playerChoice == "Paper":
        return "You win!"
      else:
       return "You Lose!"
    elif computerChoice == "Paper":
      if playerChoice == "Rock":
        return "You lose!"
      else:
        return "You win!"
    elif computerChoice == "Scissors":
      if playerChoice == "Rock":
        return "You win!"
      else:
        return "You lose!"

def main():
  playAgain="yes"
  while playAgain=="yes":
    playerChoice = input("Choose: Rock, Paper, or Scissors: ").capitalize()
    computerChoice = choices[randrange(3)]
    print("The computer chose: " + computerChoice)
    print("You chose: " + playerChoice)
    #print(playGame(playerChoice, computerChoice))
    session= playGame(playerChoice, computerChoice)
    print(session)
    print("\n\n---------------------------\n")
    playAgain = input("Do you want to play again?: ").lower()
  
  print("Thank you for Playing!")

if __name__ =="__main__":
  main()