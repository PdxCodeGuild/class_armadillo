# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. 

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# 1 yard is 0.9144 m
# 1 inch is 0.0254 m
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape", "done"]
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way', "nah"]
list_of_units = ["foot", "feet" , "ft", "'", "mile", "mile", "miles", "mi", "km", "kilometers", "kilometer", "klicks", "yards", "yds", "yard", "yd", "inches", "inch", '"', "m", "meters"] #"in",
list_of_feet = ["foot", "feet" , "ft", "'",]
list_of_miles = ["mile", "mile", "miles", "mi",]
list_of_yards = ["yards", "yds", "yard", "yd",]
list_of_inches = ["inches", "inch", '"']  #"in"
list_of_meters = ["m", "meters"]
list_of_kilometers = ["km", "kilometers", "kilometer", "klicks"]
convert_from = ""
convert_to = ""
old_distance = ""
new_distance = ""
conversion_factors = {'inches': 0.0254,
                        'feet': 0.3048,
                        'yards': 0.9144,
                        'meters': 1,
                        'miles': 1609.34,
                        'kilometers': 1000
} 




def convert_to_meters(distance):
    if convert_from in list_of_feet and convert_to in list_of_meters:
        feet_to_meters = float(distance) * 0.3048 #multiply feet by conversion factor and change to float
        feet_to_meters = round(feet_to_meters, 2) #round the decimal to 3 places 

    if convert_from in list_of_meters and convert_to in list_of_meters:
        meters_to_meters = float(distance) * 1 #multiply by conversion factor and change to float
        meters_to_meters = round(meters_to_meters, 2) #round decimal to 3 places
 
    if convert_from in list_of_yards and convert_to in list_of_meters:
        yards_to_meters = float(distance) * 0.9144 #multiply by conversion factor and change to float
        yards_to_meters = round(yards_to_meters, 2) #round decimal to 3 places
     
    if convert_from in list_of_inches and convert_to in list_of_meters:
        inches_to_meters = float(distance) * 1 #multiply by conversion factor and change to float
        inches_to_meters = round(inches_to_meters, 2) #round decimal to 3 places
  
    if convert_from in list_of_miles and convert_to in list_of_meters:
        miles_to_meters = float(distance) / 1609.34 #divide by conversion factor and change to float
        miles_to_meters = round(miles_to_meters, 2) #round decimal to 3 places
  
    if convert_from in list_of_kilometers and convert_to in list_of_meters:
        kilometers_to_meters = float(distance) / 1000 # divide by conversion factor and change to float
        kilometers_to_meters = round(kilometers_to_meters, 2) #round decimal to 3 places

def convert_from_meters(distance):
    if convert_from in list_of_meters and convert_to in list_of_feet:
        meters_to_feet = float(distance) / 0.3048 #multiply feet by conversion factor and change to float
        meters_to_feet = round(meters_to_feet, 2) #round the decimal to 3 places 

    if convert_from in list_of_meters and convert_to in list_of_meters:
        meters_to_meters = float(distance) * 1 #multiply by conversion factor and change to float
        meters_to_meters = round(meters_to_meters, 2) #round decimal to 3 places

    if convert_from in list_of_meters and convert_to in list_of_yards:
        meters_to_yards = float(distance) / 0.9144 #multiply by conversion factor and change to float
        meters_to_yards = round(meters_to_yards, 2) #round decimal to 3 places

    if convert_from in list_of_meters and convert_to in list_of_inches:
        meters_to_inches = float(distance) / 1 #multiply by conversion factor and change to float
        meters_to_inches = round(meters_to_inches, 2) #round decimal to 3 places

    if convert_from in list_of_meters and convert_to in list_of_miles:
        meters_to_miles = float(distance) * 1609.34 #divide by conversion factor and change to float
        meters_to_miles = round(meters_to_miles, 2) #round decimal to 3 places

    if convert_from in list_of_meters and convert_to in list_of_kilometers:
        meters_to_kilomters = float(distance) * 1000 # divide by conversion factor and change to float
        meters_to_kilomters = round(meters_to_kilomters, 2) #round decimal to 3 places

## calcualtes the inputted data against the conversion factor dictionary
def calculator():
        print(f"Your inputted old distance is: {old_distance}")
        print(f"Your 'convert from' unit is: {convert_from}")
        print(f"Your 'convert to' is: {convert_to}")
        old_distance = float(old_distance) * (conversion_factors[convert_from] / conversion_factors[convert_to])
        new_distance = round(old_distance, 3)
        print(new_distance)

## Attempt at returning more than one value.
def input_values():
    while True:
        while True:
            convert_from = input("What unit of measurement are we converting FROM? ")
            if convert_from in list_of_units:
                break
            else:
                print("That's not a valid response, or a unit of measurement I'm capable of converting. ")
                print("Please enter meters, kilometers, miles, feet, inches, or yards. ")
                continue        
        while True:
            convert_to = input("What unit of measurement are we converting TO? ")
            if convert_to in list_of_units:
                break
            else:
                print("That's not a valid response, or a unit of measurement I'm capable of converting. ")
                print("Please enter meters, kilometers, miles, feet, inches, or yards. ")
                continue   
        while True:
            old_distance = input("Enter distance: ")
            if not old_distance.isnumeric():
                print("That's not a valid distance. Please enter a non-negative distance. ")
            else:
                break
        break

# asks the user if they want to play again.
def play_again():
    while True:
        ask_again = input("Would you like to convert another unit? ")
        if ask_again.lower() in affirmatives:
            complete_converter()
        elif ask_again.lower() in negatives:
            print("Goodbye! ")
            break
        elif ask_again.lower() in kill_commands:
            endgame()
        else:
            print("I'm sorry, I don't understand that response. Please try again. ")

# combines ask_for_inputs() with the calculator
def complete_converter():
    while True:
        while True:
            convert_from = input("What unit of measurement are we converting FROM? ")
            if convert_from in list_of_units:
                break
            else:
                print("That's not a valid response, or a unit of measurement I'm capable of converting. ")
                print("Please enter meters, kilometers, miles, feet, inches, or yards. ")
                continue        
        while True:
            convert_to = input("What unit of measurement are we converting TO? ")
            if convert_to in list_of_units:
                break
            else:
                print("That's not a valid response, or a unit of measurement I'm capable of converting. ")
                print("Please enter meters, kilometers, miles, feet, inches, or yards. ")
                continue   
        while True:
            old_distance = input("Enter distance: ")
            if not old_distance.isnumeric():
                print("That's not a valid distance. Please enter a non-negative distance. ")
            else:
                break

        print(f"Your old distance is: {old_distance}")
        print(f"Your 'convert from' unit is: {convert_from}")
        print(f"Your 'convert to' is: {convert_to}")
        
        old_distance = float(old_distance) * (conversion_factors[convert_from] / conversion_factors[convert_to])
        new_distance = round(old_distance, 3)
        print(f"{old_distance} {convert_from} = {new_distance} {convert_to}")
        break
    play_again()

print("Welcome to the unit converter. I'm a program that coverts inches, feet, yards, meters, kilometers, and miles.")

complete_converter()
play_again()
