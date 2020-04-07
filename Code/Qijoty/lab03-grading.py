
print("hello")
print("Please enter a number representing the grade (0-100)")
num = int(input("Enter a number: "))


if num > 110:
    print("Oh wow, an A+!  You're a real scholar!")
elif num > 98:
    print("Wow, you are receiving an A!")
elif num > 94:
    print("The grade you are receiving is an A-, excellent!!")
elif num > 89:
    print("Great job, the grade you are receiving is a B+!")
elif num > 86:
    print("Alright, a B!")
elif num > 83:
    print("You are getting a B-, still okay.")
elif num > 79:
    print("The grade you are receiving is a C+, average.")
elif num > 76:
    print("You are receiving a C+")
elif num >73:
    print("You just barely made it to passing with a C-.")
elif num > 69:
    print("The grade you are receiving is a D+, yikes.")
elif num > 66:
    print("Oof, you are getting a D.")
elif num > 63:
    print("Dang, a D-...")
elif num > 59:
    print("F is for failure, did you even try?")
else:
    print("You are absolutely failing this class, maybe you should actually try next time...")

#I'm not sure I understand the concatenate aspect