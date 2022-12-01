# Class to define a player object 

import scorecard

class Player:

    # Class constructor 
    def __init__(name, index, roundCount):
        self.name = name
        self.index = index
        self.scoreCard = ScoreCard(roundCount)
