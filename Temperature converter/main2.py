""" 
    * Let's make another temperature converter after a bit of a refresher.
    * Here are a few functions to check for user error and to perform the conversion.
    * Allow the user to keep going if they would like to run the converter again without
    needing to run the code each time they want to convert.
"""

##########################################################
# Set few functions.

def converter(temp, direction): # Temperature converter and statements
    """ This function takes the user input for temperature and conversion direction, performs the math
    and generates the statement. """
    temp = float(temp)
    direction = int(direction)
    if direction == 1: # celsius to farenheit
        farenheit = temp * 9 / 5 + 32
        print(f"{temp} degrees Celsius is {farenheit} degrees Farenheit")
    if direction == 2: # farenheit to celsius
        celsius = (temp - 32) * 5 / 9
        print(f"{temp} degrees Farenheit is {celsius} degrees Celsius")

def isnumber(x): # How am I only just learning about try/except
    """ Checks if the input is a number. Returns True if so, returns False if not """
    try:
        num = float(x)
        return True
    except ValueError:
        return False

##########################################################
# Build the converter!

# Set initial variable to keep running the converter. This can be turned off at the end.
keepgoing = True

while keepgoing == True:

    # Get the input from the user of which conversion they would like to perform
    direction = input("Would you like to convert from: \n 1. Celsius to Farenheit \n 2. Farenheit to Celsius \nPlease enter 1 or 2: ")

    # Confirm that valid input was received - i.e. either 1 or 2. If not prompt user to enter again.
    while isnumber(direction) == False or float(direction) not in (1,2):
        direction = input("That's not a valid input. Please enter 1 or 2: ")

    # Get user input on the temperature they would like to convert. This must be a valid number.
    temp = input("What temperature would you like to convert? ")

    # Confirm that valid input was received. If not, prompt user to enter again.
    while isnumber(temp) == False:
        temp = input("That's not a valid temperature. Please enter a number: ")

    converter(temp, direction) # Run the converter function to perform the math and print the statement

    # Prompt user if they would like to convert again
    again = input("Would you like to convert again? Y/N: ")

    # 
    while again not in ("Y", "N"):
        again = input("That's not a valid input. Please enter Y or N: ")
    
    if again == "Y":
        keepgoing = True
    elif again == "N":
        keepgoing = False
        print("Thanks for converting with us today!")