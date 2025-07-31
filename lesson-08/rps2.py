import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))  # RPS.PAPER
# print(RPS.ROCK)  # RPS.ROCK
# print(RPS['ROCK'])  # RPS.ROCK
# print(RPS.ROCK.value)  # 1
# sys.exit()

message = '''
Enter...
1 for Rock,
2 for Paper, or
3 for Scissors

'''

playagain = True

while playagain:
    # ask user input
    playerchoice = input(message)

    player = int(playerchoice)

    # exit program on invalid user input
    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2, or 3.")

    # select random for choice for computer
    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    # control flow
    if player == RPS.ROCK.value and computer == RPS.SCISSORS.value:
        print("🎉 You win!")
    elif player == RPS.PAPER.value and computer == RPS.ROCK.value:
        print("🎉 You win!")
    elif player == RPS.SCISSORS.value and computer == RPS.PAPER.value:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 👋")
