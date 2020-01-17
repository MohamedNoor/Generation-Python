import time
import random
RPS = ["ROCK", "PAPER","SCISSORS"]
computer_chooses = random.choice(RPS)
user_chooses = str(input("pick rock, paper or scissors \n")).upper()
print("ready lets go")
time.sleep(2)
print ("rock ......")
time.sleep(2)
print ("paper ......")
time.sleep(2)
print ("Scissors......")
time.sleep(2)

if computer_chooses == "ROCK" and  user_chooses == "PAPER":
    print ("user win and computer loses \n", "user picks", user_chooses, "computer picks", computer_chooses)
elif computer_chooses == "ROCK" and user_chooses == "SCISSORS":
    print ("computer wins user loses \n", "user picks", user_chooses, "computer picks", computer_chooses)
elif computer_chooses == "PAPER" and user_chooses == "SCISSORS":
    print ("user wins computer loses\n", "user picks", user_chooses, "computer picks", computer_chooses)
elif computer_chooses == "PAPER" and user_chooses == "ROCK":
    print ("computer wins user loses \n","user picks", user_chooses, "computer picks", computer_chooses)
elif computer_chooses == "SCISSORS" and user_chooses == "PAPER":
    print ("computer wins user loses \n", "user picks", user_chooses, "computer picks", computer_chooses)
elif computer_chooses == "SCISSORS" and user_chooses == "ROCK":
    print ("user wins computer loses\n","user picks", user_chooses, "computer picks", computer_chooses)
else: print("draw user picks", user_chooses, "computer picks", computer_chooses)
