
score = float(input("What is the score: "))

ones_digit = score % 10
tens_digit = score // 10
extra = ""
if ones_digit < 5:
    print("-")
elif ones_digit >5:
    print("+")

    
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