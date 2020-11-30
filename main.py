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
print("\n-----------------------------------------")
rules = print('''Rules:
Rock: Smash Scissors, Smash Lizard

Paper: Covers Rock, Disproves Spock

Scissors: Cuts Paper, Cuts Lizard

Lizard: Eat Paper, Poison Spoke

Spock: Vaporizes Rock, Smash Scissors''')
print("-----------------------------------------\n")


# List of the options
weapons_of_mass_destruction = [rock, paper, scissors, lizard, spoke]

# Random generated weapon for bot
random_weapon = random.randint(1, len(weapons_of_mass_destruction))


def play_game():
    global random_weapon
    global user_input
    global user_input_int

    start_game_menu = ("Choose your weapon:\n"
                  "(1)- Rock\n"
                  "(2)- Paper\n"
                  "(3)- Scissor\n"
                  "(4)- Lizard\n"
                  "(5)- Spoke")
    print(start_game_menu)

    # Random generated weapon for bot
    random_weapon = random.randint(1, len(weapons_of_mass_destruction))

    while True:
        # User chooses a weapon
        user_input = input("> ")
        user_input_int = int(user_input)

        if user_input_int == 1:
            print("You played:")
            print(rock)
            bot_choice()
            break
        elif user_input_int == 2:
            print("You played:")
            print(paper)
            bot_choice()
            break
        elif user_input_int == 3:
            print("You played:")
            print(scissors)
            bot_choice()
            break
        elif user_input_int == 4:
            print("You played:")
            print(lizard)
            bot_choice()
            break
        elif user_input_int == 5:
            print("You played:")
            print(spoke)
            bot_choice()
            break
        else:
            print("Please enter a number from 1 to 5")

    # check for winners
    if user_input_int == random_weapon:
        print("It's a draw")
        play_again()
    elif user_input_int == 1 and (random_weapon == 3 or random_weapon == 4):
        print("You Won")
        play_again()
    elif user_input_int == 2 and (random_weapon == 1 or random_weapon == 5):
        print("You Won")
        play_again()
    elif user_input_int == 3 and (random_weapon == 2 or random_weapon == 4):
        print("You Won")
        play_again()
    elif user_input_int == 4 and (random_weapon == 2 or random_weapon == 5):
        print("You Won")
        play_again()
    elif user_input_int == 5 and (random_weapon == 1 or random_weapon == 3):
        print("You Won")
        play_again()
    else:
        print("You Lose")
        play_again()


# Displaying what the bot played
def bot_choice():
    global random_weapon
    print("bot played:")
    bot_turn = weapons_of_mass_destruction[random_weapon - 1]
    print(bot_turn)


def play_again():
    print("\nWould you like to play again? 'Y' or 'N'")

    while True:
        user_input_repeat = input("> ").lower()
        if user_input_repeat == "y":
            play_game()
            break
        elif user_input_repeat == "n":
            exit()
        else:
            print("Please type 'Y' or 'N'")


play_game()
