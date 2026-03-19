# BIOLOGY ISLAND
# Coded by NZ Gorham
# STARTED: 12/24/25
# UPDATED: 3/19/25

import random

# importing other Python files
# import questions

# Variables
# board = ['B', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'B', 'W', 'B', 'G', 'W', 'W', 'Y', 'B', 'W', 'W', 'W', 'Y', 'R', 'W','E']
#place = [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15,  16,  17,  18,  19,  20,  21, 22]
board = ['B', 'W', 'W', 'W', 'W', 'W', 
         'W', 'W', 'B', 'W', 'B', 'G', 'W', 'W', 'Y', 
         'B', 'W', 'W', 'W', 'Y', 'R', 'W', 
         'W', 'W', 'G', 'B', 'P', 'B', 'W', 'W', 'W', 'M', 'B', 'R', 'Y', 'W', 'B', 'G', 'Y', 'W', 
         'W', 'B', 'R', 'M', W', 'G', 
         'W', 'B', 'G', 'W', 'B', 'W', 'B', 'Y', 'W', 'W',
         'W', 'B', 'G', 'W', 'W', 'B', 'W', 'Y', 'R', 'W', 'P', 'Y', 'W', 'W', 'W', 'Y', 'R', 'W', 'W', 'M', 'W', 'W', 'B', 'G', 'Y', 'R', 'W', 'W', 'W', 'W', 'W', 'R', 'B', 'M', 'W', 'W', 'W', 'P', 'W', 'W', 'W', 'R', 'Y', 'W', 'E']
'''
  board info:
    # W = White - no questions
    # B = Blue - addition questions (Total number of blue spaces: 4)
    # R = Red - subtraction questions (Total number of red spaces: )
    # G = Green - multiplication questions (Total number of green spaces: )
    # Y = Yellow - division questions (Total number of yellow spaces: )
    # E = End - Player made it to the finish line; GAME OVER/COMPLETE
'''
position = 0
dice = random.randint(1, 6)


# RULES
print("HELLO! WELCOME TO BIOLOGY ISLAND. IN CASE IF YOU ARE WONDERING, YES. \nTHIS IS BASICALLY BOARD GAME ISLAND FROM WII PARTY. \nDO YOU WANT TO KNOW THE RULES? (TYPE YES OR NO)")
ans = input().upper() # get user input and convert to uppercase
# show rules based on user input
if (ans == "YES"):
    print("OKAY! HERE ARE THE RULES: \n1. YOU WILL ROLL A DICE TO DETERMINE HOW MANY SPACES YOU WILL MOVE. \n2. EACH SPACE HAS A COLOR THAT WILL DETERMINE WHAT TYPE OF MATH QUESTION YOU WILL GET. \n3. IF YOU ANSWER THE QUESTION CORRECTLY, YOU WILL EITHER GET TO MOVE FORWARD, STAY WHERE YOU ARE, OR MOVE BACKWARD. \n4. IF YOU ANSWER THE QUESTION INCORRECTLY, YOU WILL EITHER STAY WHERE YOU ARE OR HAVE TO MOVE BACKWARDS. \n5. THE GAME ENDS WHEN YOU REACH THE END OF THE BOARD. GOOD LUCK!\n")
elif (ans == "NO"):
    print("OKAY THEN, LET'S PLAY BIOLOGY ISLAND!\n")
else:
    print("I'M SORRY, I DIDN'T UNDERSTAND THAT. I GUESS YOU DON'T WANT TO KNOW THE RULES. \nLET'S PLAY BIOLOGY ISLAND!\n")

# GAME PLAY
# letter = board[position]
# while letter != 'E':
for letter in board:
    dice = random.randint(1, 6)
    print(letter)
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    if letter == 'B':
        qA = a
        qB = b
        print("WHAT IS", qA, "+", qB, "?")
        user_input = int(input("Your answer: "))
        if user_input == (qA + qB):
            moveup = random.randint(4, 6)
            print("Correct! You can move up ", moveup, " spaces")
        else:
            print ("Sorry. Your answer is inconrect.")
    elif letter == 'R':
        qA = a
        qB = b
        if qB > qA:
            x = qA
            qA = qB
            qB = x
        print("WHAT IS", qA, "-", qB, "?")
        user_input = int(input("Your answer: "))
        if user_input == (qA - qB):
            print("Correct!")
        else:
            moveback = random.randint(4, 6)
            print ("Sorry. Your answer is inconrect. You have to move back ", moveback, " spaces")
    elif letter == 'G':
        qA = a
        qB = b
        print("WHAT IS", qA, "*", qB, "?")
        user_input = int(input("Your answer: "))
        if user_input == (qA * qB):
            moveup = 10
            print("Correct! You can move up ", moveup, " spaces")
        else:
            print ("Sorry. Your answer is inconrect.")
    elif letter == 'Y':
        qA = a
        qB = b
        if qB > qA:
            x = qA
            qA = qB
            qB = x
        print("WHAT IS", qA, "/", qB, "? (PLEASE ROUND TO THE NEAREST HENDREDTH PLACE")
        user_input = int(input("Your answer: "))
        if user_input == (round((qA / qB), 2)):
            print("Correct!")
        else:
            moveback = 10
            print ("Sorry. Your answer is inconrect. You have to move back ", moveback, " spaces")
    elif letter == 'E':
        print("CONGRADULATIONS! YOU WIN!")
        break
    else:
        print("THIS SPACE HAS NO QUESTIONS. YOU ARE SAFE!")
