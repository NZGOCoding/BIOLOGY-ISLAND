# BIOLOGY ISLAND
# Coded by NZ Gorham
# STARTED: 11/4/26
# UPDATED: 11/6/26

# RULES, PLAYERS, & BACKGROUNDS
def rpb():
    # BACKGROUNDS
    print("HELLO! WELCOME TO BIOLOGY ISLAND. IN CASE IF YOU ARE WONDERING WHAT BIOLOGY ISLAND IS, DO YOU WANT TO LEARN ABOUT IT AND WHAT THE BEHIND THE STORY IS? (TYPE YES OR NO)")
    ans1 = input().upper()
    # show rules based on user input
    if (ans1 == "YES"):
        print("OKAY! HERE IS THE STORY BEHIND BIOLOGY ISLAND:") 
        print("IN 2020, DURING THE COVID-19 PANDEMIC, I HAD A HUGE PASSION PROJECT TO DO IN MY BIOLOGY CLASS. WE HAD THE FREEDOM TO CREATE WHAT WE WANTED TO CREATE. SO I DECIDED TO CREATE A BOARD GAME FROM THE GROUND UP AND CALLED IT: BIOLOGY ISLAND: BALANCING CHEMICAL EQUATIONS EDITION.")
        print("THE INSPIRATION BEHIND THIS CAME FROM BOARD GAME ISLAND FROM WII PARTY SINCE I BELIEVE THAT WAS THE GAME THAT I WAS PLAYING THE MOST AT THAT TIME. AS FOR WHY I DECIDED TO GO WITH BALANCING CHEMICAL EQUATIONS, I CAN'T EXACTLY REMEMBER WHY I CHOSE THAT SPECIFIC MATH...")
        print("")
        print("")
        print("NOW HOW MANY HUMANS PLAYERS ARE THERE?")
    elif (ans1 == "NO"):
        print("OKAY THEN, HOW MANY HUMANS PLAYERS ARE THERE?")
    else:
        print("I'M SORRY, I DIDN'T UNDERSTAND THAT. I GUESS YOU DON'T WANT TO KNOW ABOUT THE INSPIRATION AND STORY BEHIND BIOLOGY ISLAND THEN. HOW MANY HUMANS PLAYERS ARE THERE?")


    # NUMBER OF PLAYERS AND CPUS
    num_of_human = int(input())
    
    while (num_of_human > 4):
        print("YOU CAN ONLY HAVE 4 PLAYERS OR LESS. PLEASE ENTER HOW MANY PLAYERS ARE PLAYING:")
        num_of_human = int(input())
    
    print("OKAY. YOU HAVE ", num_of_human, " HUMAN PLAYERS PLAYING. IS THAT CORRECT? (TYPE YES OR NO)")
    ans2 = input().upper()
    # show rules based on user input
    while ((ans2 == "NO") or (ans2 == "No") or (ans2 == "no")):
        
        print("OKAY. HOW MANY HUMANS PLAYERS ARE THERE?")
        num_of_human = int(input())
        
        while (num_of_human > 4):
            print("AGAIN... YOU CAN ONLY HAVE 4 PLAYERS OR LESS. PLEASE ENTER HOW MANY PLAYERS ARE PLAYING:")
            num_of_human = int(input())
            
        print("OKAY. YOU HAVE ", num_of_human, " HUMAN PLAYERS PLAYING. IS THAT CORRECT? (TYPE YES OR NO)")
        ans2 = input().upper()
    
    if (num_of_human == 4):
        num_of_cpu = 0
        print("SINCE YOU HAVE", num_of_human, ", YOU CAN'T HAVE ANY CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
        
    elif (num_of_human == 3):
        num_of_cpu = 1
        print("SINCE YOU HAVE", num_of_human, ", YOU CAN HAVE", num_of_cpu, "CPU PLAYER. BEFORE WE GET ONTO THE RULES, YOU HAVE THE OPTION TO HAVE 1 CPU PLAYER OR 0 CPU PLAYERS. SO, WOULD YOU LIKE TO CHANGE THE NUMBER OF CPU PLAYERS? (TYPE YES OR NO)")
        ans2_2 = input().upper()
        # show rules based on user input
        while ((ans2_2 == "YES") or (ans2_2 == "Yes") or (ans2_2 == "yes")):
            print("OKAY. HOW MANY CPU PLAYERS DO YOU WANT? YOU CAN CHOOSE 0 OR 1")
            num_of_cpu = int(input())
            
            while (num_of_cpu > 1):
                print("YOU CAN ONLY CHOOSE 0 OR 1. PLEASE CHOOSE 0 OR 1:")
                num_of_cpu = int(input())
                
            print("OKAY. YOU HAVE ", num_of_cpu, " CPU PLAYERS PLAYING. WOULD YOU LIKE CHANGE? (TYPE YES OR NO)")
            ans2_2 = input().upper()
        if (num_of_cpu == 0):
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
        else:
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYER. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
            
    elif (num_of_human == 2):
        num_of_cpu = 2
        print("SINCE YOU HAVE", num_of_human, ", YOU CAN HAVE", num_of_cpu, "CPU PLAYER. BEFORE WE GET ONTO THE RULES, YOU HAVE THE OPTION TO HAVE 2, 1, OR 0 CPU PLAYERS. SO, WOULD YOU LIKE TO CHANGE THE NUMBER OF CPU PLAYERS? (TYPE YES OR NO)")
        ans2_2 = input().upper()
        # show rules based on user input
        while ((ans2_2 == "YES") or (ans2_2 == "Yes") or (ans2_2 == "yes")):
            print("OKAY. HOW MANY CPU PLAYERS DO YOU WANT? YOU CAN CHOOSE 0, 1, OR 2")
            num_of_cpu = int(input())
            
            while (num_of_cpu > 2):
                print("YOU CAN ONLY CHOOSE 0, 1, OR 2. PLEASE CHOOSE 0, 1, OR 2:")
                num_of_cpu = int(input())
                
            print("OKAY. YOU HAVE ", num_of_cpu, " CPU PLAYERS PLAYING. WOULD YOU LIKE CHANGE? (TYPE YES OR NO)")
            ans2_2 = input().upper()
        if (num_of_cpu == 0):
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
        elif (num_of_cpu == 1):
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYER. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")        
        else:
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
                
    else:
        num_of_cpu = 3
        print("SINCE YOU HAVE", num_of_human, ", YOU CAN HAVE", num_of_cpu, "CPU PLAYER. BEFORE WE GET ONTO THE RULES, YOU HAVE THE OPTION TO HAVE 3, 2, OR 1 CPU PLAYERS. SO, WOULD YOU LIKE TO CHANGE THE NUMBER OF CPU PLAYERS? (TYPE YES OR NO)")
        ans2_2 = input().upper()
        # show rules based on user input
        while ((ans2_2 == "YES") or (ans2_2 == "Yes") or (ans2_2 == "yes")):
            print("OKAY. HOW MANY CPU PLAYERS DO YOU WANT? YOU CAN CHOOSE 0, 1, OR 2")
            num_of_cpu = int(input())
            
            while ((num_of_cpu > 3) or (num_of_cpu < 1)):
                print("YOU CAN ONLY CHOOSE 0, 1, OR 2. PLEASE CHOOSE 0, 1, OR 2:")
                num_of_cpu = int(input())
                
            print("OKAY. YOU HAVE ", num_of_cpu, " CPU PLAYERS PLAYING. WOULD YOU LIKE CHANGE? (TYPE YES OR NO)")
            ans2_2 = input().upper()
        if (num_of_cpu == 0):
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
        elif (num_of_cpu == 1):
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYER. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")        
        else:
            print("SINCE YOU HAVE", num_of_human, ", AND", num_of_cpu, "CPU PLAYERS. SO NOW ONTO THE RULES. WOULD YOU LIKE TO LEARN ABOUT THE RULES? (TYPE YES OR NO)")
                
    
    # RULES
    ans3 = input().upper() # get user input and convert to uppercase
    # show rules based on user input
    if (ans3 == "YES"):
        print("OKAY! HERE ARE THE RULES:") 
        print("1. YOU WILL ROLL A DICE TO DETERMINE HOW MANY SPACES YOU WILL MOVE.")
        print("2. EACH SPACE HAS A COLOR THAT WILL DETERMINE WHAT TYPE OF MATH QUESTION YOU WILL GET.")
        print("3. IF YOU ANSWER THE QUESTION CORRECTLY, YOU WILL EITHER GET TO MOVE FORWARD, STAY WHERE YOU ARE, OR MOVE BACKWARD.")
        print("4. IF YOU ANSWER THE QUESTION INCORRECTLY, YOU WILL EITHER STAY WHERE YOU ARE OR HAVE TO MOVE BACKWARDS.")
        print("5. THE GAME ENDS WHEN YOU REACH THE END OF THE BOARD. GOOD LUCK!\n")
    elif (ans3 == "NO"):
        print("OKAY THEN, LET'S PLAY BIOLOGY ISLAND!\n")
    else:
        print("I'M SORRY, I DIDN'T UNDERSTAND THAT. I GUESS YOU DON'T WANT TO KNOW THE RULES. \nLET'S PLAY BIOLOGY ISLAND!\n")
        
        
    return num_of_human, num_of_cpu
