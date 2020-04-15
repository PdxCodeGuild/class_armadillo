# My grading Lab.

# This is for inputting the numerical grade (score) 0 - 100 to generate a letter grade. The float is to show any decible points.
score = float(input("What is the score: "))

# Thise section is to differentiate between the one's position and the 10's position 
ones_digit = score % 10
tens_digit = score // 10
extra = ""

# This if statement takes the % and // from the section above and uses it to add either a - or a + to the letter grade
if ones_digit < 5:
    print("-")
elif ones_digit >5:
    print("+")

# This section is the main part of the program that takes the numerical grade (score) that was entered by the user and changes it to a letter grade. 
if score >= 90 and score <= 100:
    print("A")

elif score >= 80 and score <= 89:
    print("B")

elif score >= 70 and score <= 79:
    print("C")

elif score >= 60 and score <= 69:
    print("D")
   
elif score >= 0 and score <=59:
     print("F")

else:
    print("Score are between 0 and 100")