# yahtzee rules: http://yahtzee-rules.com/

# Main execution context
def main (): 

    # Local Variable Declaration 
    userInput = ""
    playerCount = 0
    roundCount = 0
    
    # Get user input from the command line 
    userInput = input("Enter a number from 1-10 ('q' to quite): ")

    # Main event loop
    while userInput != 'q': 
        # Print the user's input 
        print(f"You entered: {userInput}")

        # Get user input from the command line 
        userInput = input("Enter a number from 1-10 ('q' to quite): ")

def calculateGameScore():
    #
    print ("TO DO")
# Call main to start the program 
main()