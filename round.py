# Script to manage a round. Within a round the player(s) will take turns until 
# their score cards are filled up. This should take 13 rounds.

import turn 
from player import Player

def doRound (players: list[Player]): 
    
    # Local Variable Declaration 
    finishedPlayers = [Player]
        
    # For each round have all the players take turns until their score 
    # cards are filled 
    while len(players) > 0 :
    
        # Loop through all the players 
        for player in players: 
            
            # Have each player take a turn 
            turn.doTurn(player)

            # If the player's scorecard is filled move the player to 
            # finished list
            if player.scoreCard.roundIsFilled(): 

                # DEBUG: Is there a secenario where the players wont finish 
                # in the order that they were played?
                finishedPlayers.append(players.pop(0))
                #players.remove(player)
  
    
    # Return the finished players 
    return finishedPlayers


