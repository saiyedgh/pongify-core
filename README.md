# Pongify - your table tennis game manager

## Documentation

- Pongify is a program written in vanilla Python – majority of the code.
- It is a is a table tennis schedule manager and points/result calculator.
- Pongify only features games and tournaments for 2 to 5 players.
<br>

## Run the program

- Copy all the contents of the `pongify.py` file, then paste the content into a Google Collab python file.
- Or, install the `Python` extension on **VS Code** and run using the *play* button icon on the top right corner of VS Code.
- Alternatively, you can access **Jupyter** notebook and upload, then run the file.

Pongify's code logic is divided into three main parts:
## Part 01 - Scheduler
- Firstly, it takes user input for the number of players, from *two* to *five*.
- Based on the number of players, it asks the name of each player, capturing the player names in a list called "**players**".

- Pongify then asks for number of rounds which decides how many matches will the players play with the other(s).
- The program then creates player combinations using Python [itertools](https://docs.python.org/3/library/itertools.html) library.
<br>

## Part 02 - Points Table

Pongify then creates a points table (a 2d list) to account for:

- Player names based on the user input from *Part 01*,
- Player points scored - points for "**PF**",
- Player points received - points against "**PA**",
- Player points difference "**PD**",
- Player Wins/Losses - "**W**" / "**L**",
- Total player "**Points**" - 3 points for each win.
<br>

## Part 03 - Match Results and Player Standing

- Pongify then calculates results, match by match.
- It asks for match results doumenting each player's score.
- It then calculates the win/loss and the points situation and edits the points table.
- It prints the results till the last match and player score then outputs the points table where the players can check the results.

## Game Rules

- Table tennis rules [https://www.pongfit.org/official-rules-of-table-tennis](https://www.pongfit.org/official-rules-of-table-tennis).
- At 11 points if a player has a two point advantage, they win.

## Example Tournament

**To test the program, following is a sample game scenario:**

- Number of players: 3
- Enter three player names:
    - player 1: "*Anas*"
    - player 2: "*Hassan*"
    - player 3: "*Syed*"
- Number of rounds: 1

**Enter results:**

- Match 01 -> *Anas* = 11, *Hassan* 9 (*Anas* wins by two points),
- Match 02 -> *Anas* = 15, *Syed* 13 (*Anas* wins again),
- Match 03 -> *Hassan* = 11, *Syed* 7 (*Hassan* wins by 4 points),
- Match 04 -> *Anas* = 11, *Hassan* 5 (*Anas* wins by 6 points),
- Match 05 -> *Anas* = 9, *Syed* 11 (*Syed* wins by 2 points),
- Match 06 -> *Hassan* = 15, *Syed* 13 (*Hassan* wins by 2 points),
- *Anas* should win having 9 match points in total, followed by 6 points for *Hassan*, and 3 points for *Syed*.

## Limitations and upcoming Improvements

- Is limited to single player names not doubles or teams, can be improved to incorporate teams and member names.
- The current setup does not support editing/updating or deleting results, can add that functionality.
- The command line interface is not user friendly, can use **Flask** or **Django** to create a web based UI written in Python.
- Need to improve code validation.
- Can validate and make sure player names are only strings.
- Can store calculation logic in a function and use it for the other.
- The list is not sorted based on results and standings.
- The final points table rows can be sorted based on points and points difference.


## Project Details

Faculty: Faculty of Information.
University: University of Toronto.
Program: BI – Bachelor of Information.
Course: INF452 - Information Design V - Coding.
Instructor: Dr. Maher Elshakankiri.
Student: Syed-Mughira Hassan.
Assignment: Mid-term.
Programming Language: Python.
Date Created: 31-Oct-2023.
Date Modified: 04-Nov-2023.