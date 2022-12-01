# Class (Struct) to define the all the categories of the score card. All a 
# plyer's scores for a whole game (3 rounds) are store in this object 

class ScoreCard: 
    def __init__(roundCount):
        self.rounds = [ dict.fromkeys(scorableCombos, initialComboVals) ]

        # Loop through to the round count adding rounds 
        for round in range(0, roundCount):
            self.rounds.append(dict.fromkeys(scorableCombos, initialComboVals))


# Dictionary to define the categaries to score in for each round 
scorableCombos = ("one", "two", "three", "four", "five", "six", "pair", )
initialComboVals = ""