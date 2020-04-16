#    Version 1

#    Have the user enter a number representing the grade (0-100)
#    Convert the number grade to a letter grade

#   I/O User Letter grade strings

num = input("Enter your Grade: ")
num = int(num)

if num > 89:
    str1 = "A"
elif num > 79 and  90:
    str1 = "B"
elif num > 69 and  80:
    str1 = "C"
elif num > 59 and  70:
    str1 = "D"
elif num > 19 and  60:
    str1 = "F"

#   I/O User Specific grade strings

if num != 100 and num >59 and num % 10 < 5:
   str2 = "-"
elif num > 59 and num % 10 > 4:
    str2 = "+"
elif num == 100:
    str2 = "+"
else:
    str2 = ""

#   Prints specific grade

print (str1 + str2)