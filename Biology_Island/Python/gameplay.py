def game_play():
    # Variables
    mainBoard = ['B', 'W', 'W', 'W', 'W', 'W','W', 'W', 'B', 'W', 'B', 'G', 'W', 'W', 'Y',
            'B', 'W', 'W', 'W', 'Y', 'R', 'W',
            'W', 'W', 'G', 'B', 'P', 'B', 'W', 'W', 'W', 'M', 'B', 'R', 'Y', 'W', 'B', 'G', 'Y', 'W',
            'W', 'B', 'R', 'M', 'W', 'G',
            'W', 'B', 'G', 'W', 'B', 'W', 'B', 'Y', 'W', 'W',
            'W', 'B', 'G', 'W', 'W', 'B', 'W', 'Y', 'R', 'W', 'P', 'Y', 'W', 'W', 'W', 'Y', 'R', 'W', 'W', 'M', 'W', 'W', 'B', 'G', 'Y', 'R', 'W', 'W', 'W', 'W', 'W', 'R', 'B', 'M', 'W', 'W', 'W', 'P', 'W', 'W', 'W', 'R', 'Y', 'W', 'E']
    '''
    main board info:
        # W = White - no questions
        # B = Blue - addition questions (Total number of blue spaces: 4)
        # R = Red - subtraction questions (Total number of red spaces: )
        # G = Green - multiplication questions (Total number of green spaces: )
        # Y = Yellow - division questions (Total number of yellow spaces: )
        # M = Mix - the question is either addition or subraction. If addition and player answers correct, they move up 7 spaces. If subtraction and player answers incorrect, they move back 7 spaces (Total number of yellow spaces: 4)
        # P = Purple - make you move 20 spaces back (Total number of yellow spaces: 3)
        # E = End - Player made it to the finish line; GAME OVER/COMPLETE
    '''
    position = 0
    dice = random.randint(1, 6) # This will be saved for later
    
    # letter = board[position]
    # while letter != 'E':
    for letter in mainBoard:
        dice = random.randint(1, 6) # This will be saved for later
        print(letter)
        qA = random.randint(0, 100)
        qB = random.randint(0, 100)
        if letter == 'B':
            print("WHAT IS", qA, "+", qB, "?")
            user_input = int(input("Your answer: "))
            if user_input == (qA + qB):
                moveup = random.randint(4, 6)
                print("Correct! You can move up ", moveup, " spaces")
            else:
                print ("Sorry. Your answer is inconrect.")
        elif letter == 'R':
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
            print("WHAT IS", qA, "*", qB, "?")
            user_input = int(input("Your answer: "))
            if user_input == (qA * qB):
                moveup = 10
                print("Correct! You can move up ", moveup, " spaces")
            else:
                print ("Sorry. Your answer is inconrect.")
        elif letter == 'Y':
            if qB > qA:
                x = qA
                qA = qB
                qB = x
            print("WHAT IS", qA, "/", qB, "? (PLEASE ROUND TO THE NEAREST HENDREDTH PLACE")
            user_input = int(input("Your answer: "))
            if user_input == (round((qA / qB))):
                print("Correct!")
            else:
                moveback = 10
                print ("Sorry. Your answer is inconrect. You have to move back ", moveback, " spaces")
        elif letter == 'M':
            if qB > qA:
                x = qA
                qA = qB
                qB = x
                print("WHAT IS", qA, "-", qB, "?")
                user_input = int(input("Your answer: "))
                if user_input == (qA - qB):
                    print("Correct!")
                else:
                    moveback = 7
                    print ("Sorry. Your answer is inconrect. You have to move back ", moveback, " spaces")
            else:
                print("WHAT IS", qA, "+", qB, "?")
                user_input = int(input("Your answer: "))
                if user_input == (qA + qB):
                    moveup = 7
                    print("Correct! You can move up ", moveup, " spaces")
                else:
                    print ("Sorry. Your answer is inconrect.")
        elif letter == 'P':
            print("OH NO! YOU ARE GOING TO THE POISON BOARD!")
            poison_board()
        elif letter == 'E':
            print("CONGRADULATIONS! YOU WIN!")
            break
        else:
            print("THIS SPACE HAS NO QUESTIONS. YOU ARE SAFE!")

# POISON BOARD
def poison_board():
    poisonBoard = ['B', 'W', 'B', 'I', 'W', 'W', 'W', 'W', 'L']
    '''
    poision board info:
        # W = White - no questions (Total number of red spaces: 1)
        # B = Blue - addition questions (Total number of blue spaces: 2)
        # I = Red - subtraction questions (Total number of red spaces: 1)
        # L = Green - multiplication questions (Total number of green spaces: 1)
    This will be saved for later
    '''
    for letter in poisonBoard:
        dice = random.randint(1, 6) # This will be saved for later
        print(letter)
        qA = random.randint(0, 100)
        qB = random.randint(0, 100)
        if letter == 'B':
            print("WHAT IS", qA, "+", qB, "?")
            user_input = int(input("Your answer: "))
            if user_input == (qA + qB):
                moveup = random.randint(3, 4)
                print("Correct! You can move up ", moveup, " spaces")
            else:
                print ("Sorry. Your answer is inconrect.")
        elif letter == 'I':
            print("Congradulations! You made it out of the poison board early! Back you go back to the main board")
        elif letter == 'L':
            print("Congradulations! You made it out of the poison board! Back you go back to the main board")
        else:
            print("THIS SPACE HAS NO QUESTIONS. YOU ARE SAFE!")
