## Temperature converter project

# Create a program that takes user input 
# Ask user which way to convert (C to F or F to C) with options, user enters which they want
# Take input in form of number with a F or C at the end, then converts to the other one.
# Then loops back and offers again until the user exits

# Make it make sense and try to make them laugh

# Try to figure out git for bonus points and then cry when you can't get it

#-----------------------------------------------------------------------------------------------------------------------
# F U N C T I O N   T I M E

# Function "converter" converts the temperature between F and C or C and F depending on the chosen starting unit
# Users will either choose 0 for F to C or 1 for C to F
def converter(unit, temp, neg):

    if unit == 0:
        # Conversion from Fahrenheit to Celcius
        C = int(5 * (temp*neg - 32) / 9)
        print(f"{temp*neg}F is {C}C")

    if unit == 1:
    # Conversion from Celcius to Fahrenheit
        F = int((9 * temp*neg / 5) + 32)
        print(f"{temp*neg}C is {F}F")

#-----------------------------------------------------------------------------------------------------------------------
# U S E R   I N P U T   T I M E

# User input statements to determine starting unit and integer. Let's account for entering something valid and not valid.
# If it's a number, great. We can handle that easily.
# Anything else, give 'em hell.

print("Hello it's me, your friendly neighbourhood temperature converter! Give me an integer to convert to Fahrenheit or Celcius.")

itsago = True #its a me, for the while loop!

# Keep running this loop until the user choses to exit.
while itsago == True:

    # Grab input on what type of conversion the user wants.
    unit = input("What type of conversion would you like to perform? \n     0: Fahrenheit to Celcius \n     1: Celcius to Fahrenheit \nPlease enter 0 or 1. ")
    
    # You kooky kids, check we have valid input and keep asking for it until you do it.
    while unit != "0" and unit != "1":
        unit = input("What the.. what? What are you doing? \n     0: Fahrenheit to Celcius \n     1: Celcius to Fahrenheit \nChoose 0 or 1: ")
   
    # Turn that into an int now. Do we need to? I guess not? But it feels right to not have it as a string.
    unit = int(unit)
    neg = 1

    # Custom statements to confirm the user's choice and ask for the number to convert.
    if unit == 0:
        temp = input("You got it coach! We're going F to C. \nNow, what number would you like to convert from Fahrenheit to Celcius? ")
        while str.isdigit(temp) == False:
            # Check if it's just a negative number.
            if temp[0] == "-":
                if str.isdigit(temp[1:]) == True:
                    temp = temp[1:]
                    neg = -1
            else:
                temp = input("Come on, that's not a number. Give me just a digit to convert from F to C: ")

    if unit == 1:
        temp = input("You got it coach! We're going C to F. \nNow, what number would you like to convert from Celcius to Fahrenheit? ")
        while str.isdigit(temp) == False:
            # Check if it's just a negative number.
            if temp[0] == "-":
                if str.isdigit(temp[1:]) == True:
                    temp = temp[1:]
                    neg = -1
            else:
                temp = input("Come on, that's not a number. Give me just a digit to convert from F to C: ")

    temp = int(temp)

    print("Thanks, bud. Let's do this thing.")

    converter(unit, temp, neg)

    # So uh, we still going? Figure out if we're looping again and change itsago if we need to exit.

    more = input("Anutha one? (yes/no) ")

    # Back to input if we get an answer we can't use until the user gives us something we can.
    while more != "yes" and more != "no":
        more = input("Come on, you know better. Enter something I can use. \nAnutha one? (yes/no) ")

    # Use the answer to run another loop or crash out.
    if more == "yes":
        print("One! More! Time!")
        itsago = True
    elif more == "no":
        print("Smell ya later!")
        itsago = False
    else:
        print("The call is coming from inside the house. call 911")

