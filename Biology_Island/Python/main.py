# BIOLOGY ISLAND: ELEMENTARY MATH EDITION
# Coded by NZ Gorham
# STARTED: 12/24/25
# UPDATED: 11/4/26

import random
import rules
import gameplay

# I used Geeks for Geeks to learn how to create a main function in python
# Defining main function
def main():
    # RULES, PLAYERS, & BACKGROUNDS
    human, cpu = rules.rpb()
    
    # GAME PLAY
    gameplay.game_play(human, cpu)    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
