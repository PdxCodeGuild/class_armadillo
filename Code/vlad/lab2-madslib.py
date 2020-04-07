#Lab: 2 Mads Lib
keep_running = 'yes'
while keep_running == 'yes':
    champ = input("How many titles have lebron james won: ")
    feel = input("Enter how Jordan should feel: ")
    sport = input("Enter what nba team does lebron james play for: ")
    madlib = f"""
        LeBron won  {champ} titles.  I think Michael Jordan should feel {feel} 
        if LeBron continue to win NBA titles and become the champion in the next seasons, 
        LeBron will pass MJ and become the ultimate GOAT without any argument!
        And what about Shaq? he should feel {feel} about LeBron success? 
        After all, LeBron is clearly the NBA King (not the tiger king :) 
        Bron is the best Player in the {sport}
    """
    print(madlib)

    keep_running = input('Would you like to try it again? yes/no: ')