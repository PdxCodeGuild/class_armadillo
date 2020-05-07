
#    Have the user enter a number representing the grade (0-100)
#    Convert the number grade to a letter grade

#    User Letter grade strings

num = input("Enter your Grade: ")
num = int(num)

if num > 89:
    str1 = ("A")
elif num > 79 and  90:
    str1 = ("B")
elif num > 69 and  80:
    str1 = ("C")
elif num > 59 and  70:
    str1 = ("D")
elif num > 19 and  60:
    str1 = ("F")

#    User specific grade strings

if num % 10 < 5 and num != 100 and num >59:
   str2 = ("-")
if num % 10 > 4 and num > 59:
    str2 = ("+")
if num == 100:
    str2 = ("+")
else:
    str2 = ("")

#    String concatenation

print (str1 + str2)