# Class to define a player object 

from scorecard import ScoreCard

class Player:

    # Class constructor 
    def __init__(self, name, index, roundCount):
        self.name = name
        self.index = index
        self.scoreCard = ScoreCard(roundCount)
