# Instructions
# Search the interwebs for an example Mad Lib
# Ask the user for each word you'll put in your Mad Lib
# Use string concatenation to put each word into the Mad Lib

champ = input("How many title LeBron won: ")
feel = input("enter how Jordan should feel: ")
sport = input("Enter the name of the sport LeBron James currently play: ")

madlib = f"""
LeBron won  {champ} titles.  I think Michael Jordan should {feel} if LeBron will continue to pass him and breaking his record.

And what about Shaq? he should feel {feel} that LeBron success? After all, LeBron is clearly best current Player in the {sport}
"""
print(madlib)