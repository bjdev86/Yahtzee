# Main execution context
def main (): 

    # Local Variable Declaration 
    userInput = ""

    # Get user input from the command line 
    userInput = input("Enter a number from 1-10 ('q' to quite): ")

    # Main event loop
    while userInput != 'q': 
        # Print the user's input 
        print(f"You entered: {userInput}")

        # Get user input from the command line 
        userInput = input("Enter a number from 1-10 ('q' to quite): ")

# Call main to start the program 
main()