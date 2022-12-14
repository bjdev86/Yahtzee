# yahtzee rules: http://yahtzee-rules.com/
# https://www.officialgamerules.org/yahtzee

import round
from player import Player

# Main execution context
def main (): 

    # Local Variable Declaration 
    userInput = ""
    playerCount = 0
    roundCount = 0
    finishedPlayers = [Player]
    
    # Get user input from the command line 
    userInput = input("Enter a number from 1-10 ('q' to quite): ")

    # Main game loop
    while userInput != 'q': 
       
        # Ask the user for how many players will be playing this game 
        playerCount = input("How many players for this game: ")

        # Build player collection (How to instansiate a list of blank players)
        players = [Player]

        # Ask the user for the round count 
        roundCount = input("How many rounds do you wanna play: ")

        # Round loop 
        for i in range(roundCount): 
            
            # Preform the round 
            finishedPlayers = round.doRound(players)

            # Print the scorecard round (ie the column that was just filled out)
            print(f"ROUND OVER: \n {printRound(finishedPlayers)}")

        # Get user input from the command line 
        userInput = input("Enter a number from 1-10 ('q' to quite): ")

def calculateGameScore():
    
    #
    pass

# Function to stringify the results of finishing a column representing a 
# completed round in the game.
def printRound(round, finishedPlayers: list[Player]): 

    # Local Variable Declaration 
    rndScoreTxt = ""

    # Loop through all the players access their scorecards and get the round 
    # column
    for player in finishedPlayers: 
        player.scoreCard.getRoundScores(round)

    return rndScoreTxt

# Call main to start the program 
main()
