Lab 3: Grading
# Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

# Concepts Covered
# input, print
raw_score = input("What did you get on your test?")
# type conversion (str to int)
digit_score = int(input)
# comparisons (< <= > >=)
if digit_score > 90 and digit_score <= 100:
    print("A")
elif digit_score > 80 and digit_score <= 89:
    print("B")
elif digit_score > 70 and digit_score <= 79:
    print("C")
elif digit_score > 60 and digit_score <= 69:
    print("D")
else:
    print("Please retake the test")
