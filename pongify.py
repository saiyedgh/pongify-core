# ----------------------- Pongify - Program ----------------------- #

# ----------------------- Imports #
# Requiring itertools library for alternative looping to create player combinations
# https://docs.python.org/3/library/itertools.html
import itertools

# ----------------------- Part 01 - Scheduler ----------------------- #
print("") # will use this syntax to print linebreaks for CLI/Game readability

# Input loop to capture player names 
while True:
    try: # try to catch integer input
        numPlayers = int(input("Enter number of players from (2-5): "))
        # limiting player range from to 2 - 5
        if numPlayers >= 2 and numPlayers <= 5: # valid input
            break
        else: # condition error message
            print("Must have 2 to 5 players.")
    except ValueError: # loop error message
        print("Please enter a valid number.")

players = []

print("")

# Capture player names and edit the players list
for i in range(numPlayers):
    userInput = input(f"Enter player name {i + 1}: ")
    players.append(userInput)

# Asking for number of rounds
while True:
    try:
        print("")
        # explaining the idea of match rounds
        print("One round = two matches with each player")
        print("")
        # adding 1 to user because one round equals two games with each
        rounds = int(input("Enter number of rounds from (1-3): ")) + 1
        # tournament round limit 
        if rounds >= 1 and rounds <= 3:
            break
        else: # condition error message
            print("Must have 1, 2 or 3 rounds.")
    except ValueError: # loop error message
        print("Please enter a valid number.")

# Printing the number of player matches with the other player(s)
print(f"Matches vs each: {rounds}")

# Creating a function that takes a list of names and number of rounds and creates match combinations
def playerCombinations(playerList, matchRounds):
    combinations = []
    # the loop does not require an iterator variable as that is managed by the itertools library
    for _ in range(matchRounds):
        #https://www.geeksforgeeks.org/itertools-combinations-module-python-print-possible-combinations/
        roundCombinations = list(itertools.combinations(playerList, 2))
        combinations.extend(roundCombinations)
    return combinations # value accessible for use

combinations = playerCombinations(players, rounds)

matchList = []

# Taking the combination list and destructuring the input to create our custom nested list called "matchList"
# using enumerate to adjust the array index and sequence
# https://www.w3schools.com/python/ref_func_enumerate.asp
for sequence, (player1, player2) in enumerate(combinations, start=1):
    matchList.append([player1, player2])

# Printing the player match details
print("")
print("**** Table Tennis game tournament schedule ****")
print(f"Each player plays {rounds} matches with the other player(s):")
print("")

# Printing the tournament schedule
# using enumerate with the for loop for easy indexing
for index, item in enumerate(matchList):
    player01 = item[0]
    player02 = item[1]
    print(f"Match {index + 1}: {player01} vs {player02}")

# ----------------------- Part 02 - Points Table ----------------------- #

# Creating a 2d list with table headers
tableHeader = ["Name", "W", "L", "PF", "PA", "PD", "Points"]
pointsTable = [tableHeader] 

# Adding the list rows with player names in the first column and 0s in all the others as a numeric placeholder
for name in players:
    row = [name] + [0] * (len(tableHeader) - 1)
    pointsTable.append(row)

# ----------------------- Part 03 - Match Results and Player Standing ----------------------- #

matchIndex = int(1) # initiating a match counter

# looping through the match list to make changes to the points table according to each match
for match in matchList:
    # temp variable to capture player scores
    # will be used for points table calculations
    player01Score = int() 
    player02Score = int()
    
    # printing mere linebreak and some text
    print("")
    print("Points table: ")

    # Printing results before and after each match
    for row in pointsTable:
        print(row)
    print("")

    # Printing the match details Player01 vs Player02
    print(f"Match {[matchIndex]}: {match[0]} vs {match[1]}")
    matchIndex += 1 # add 1 to counter after each match

    # Each match calculation
    # looping through each match players and record their score
    for matchPlayer in match:
        # keep asking for a valid input
        while True:
            try:
                print("")
                # Asking for player score
                inputValue = int(input(f"Enter match score of {matchPlayer}: "))
                # the scores don't usually cross 20 points, hence, 30 is a good limit
                if inputValue <= 30:
                    # first player score
                    if matchPlayer == match[0]:
                        player01Score = inputValue
                    # second player score
                    else:
                        player02Score = inputValue
                    break  # Exit the loop if a valid integer score is provided
                else: # condition error message
                    print("Points must be less than 30")
            except ValueError: # while loop error message
                print("Invalid input. Please enter an integer value.")

    # Points table calculation based on the player01Score and player02Score
    # looping through the points table and edit results based on match score input
    for row in pointsTable[1:]: #skipping the table headers
        # match player names and calculate player 01 results
        if row[0] == match[0]:
            row[3] += player01Score # Points for - PF
            row[4] += player02Score # Points against - PA
            row[5] = row[3] - row[4] # Points difference - PD
            # if player01 won
            if player01Score > player02Score:
                row[1] += 1  # Increase 'W' or win for player01Score
            # if player01 lost
            else:
                row[2] += 1  # Increase 'L' or loss for the player
            # Update the Points column based on player win
            row[6] = row[1] * 3  
        
        # match player names and calculate player 02 results
        elif row[0] == match[1]:
            row[3] += player02Score # Points for - PF
            row[4] += player01Score # Points against - PA
            row[5] = row[3] - row[4] # Points difference - PD
            # if player02 won
            if player02Score > player01Score:
                row[1] += 1  # Increase 'W' or win for player02Score
            # if player02 lost
            else:
                row[2] += 1  # Increase 'L' or loss for the player
            # Update the Points column based on player win
            row[6] = row[1] * 3  

# Print the Final result
print("")
print("**** The Final Result ****")
# taking the results from the Points Table
for row in pointsTable:
    print(row)

print("")
