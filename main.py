import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

spoke = '''                                                                                 
        @@@        @@@@                 
        @@@@       @@@@ @@@@            
    @@@%@@@@@      @@@@@@@@@            
     @@@ @@@@     @@@@@@@@@             
     @@@@ @@@@    @@@@ @@@@             
      @@@ @@@@@  @@@@ @@@@/             
      @@@@@@@@@@@@@@@@@@@@              
      @@@@@@@@@@@@@@@@@@@@              
      @@@@@@@@@@@@@@@@@@@@      @@@@@@  
      @@@@@@@@@@@@@@@@@@@@   @@@@@@@@   
       @@@@@@@@@@@@@@@@@@@@@@@@@@       
       @@@@@@@@@@@@@@@@@@@@@@@@         
       @@@@@@@@@@@@@@@@@@@@@&           
        @@@@@@@@@@@@@@@@@@              
         @@@@@@@@@@@@@@@                               
'''

lizard = '''                                                                                                          
  _      _____ ______         _____  _____  
 | |    |_   _|___  /   /\   |  __ \|  __ \ 
 | |      | |    / /   /  \  | |__) | |  | |
 | |      | |   / /   / /\ \ |  _  /| |  | |
 | |____ _| |_ / /__ / ____ \| | \ \| |__| |
 |______|_____/_____/_/    \_\_|  \_\_____/                                                                                                     
'''


# MARK: - RULES:
    #Rock: Smash Scissors, Smash Lizard
    #Paper: Covers Rock, Disproves Spock
    #Scissors: Cuts Paper, Cuts Lizard
    #Lizard: Eat Paper, Poison Spoke
    #Spock: Vaporizes Rock, Smash Scissors

# List of the options
weapons_of_mass_destruction = [rock, paper, scissors, lizard, spoke]

start_game = print("Choose your weapon:\n" 
                  "(1)- Rock\n" 
                  "(2)- Paper\n"
                   "(3)- Scissor\n"
                   "(4)- Lizard\n"
                   "(5)- Spoke")

user_input = input("> ")

if int(user_input) == 1:
    print("You played:")
    print(rock)
elif int(user_input) == 2:
    print("You played:")
    print(paper)
elif int(user_input) == 3:
    print("You played:")
    print(scissors)
elif int(user_input) == 4:
    print("You played:")
    print(lizard)
elif int(user_input) == 5:
    print("You played:")
    print(spoke)
else:
    print("Please enter a number from 1 to 5")

# Random generated weapon for bot
random_weapon = random.randint(0, len(weapons_of_mass_destruction)-1)
print("bot played:")
bot_turn = print(weapons_of_mass_destruction[random_weapon])
bot_input = random_weapon + 1
user_input_int = int(user_input)



# check for winners
if user_input_int == bot_input:
    print("It's a draw")
elif user_input_int == 1 and (bot_input == 3 or bot_input == 4):
    print("You Won5")
elif user_input_int == 2 and (bot_input == 1 or bot_input == 5):
    print("You Won")
elif user_input_int == 3 and (bot_input == 2 or bot_input == 4):
    print("You Won")
elif user_input_int == 4 and (bot_input == 2 or bot_input == 5):
    print("You Won")
elif user_input_int == 5 and (bot_input == 1 or bot_input == 3):
    print("You Won")
else:
    print("You Lose")





