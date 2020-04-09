


# this is what number you want to switch to a letter grade
num = input("Enter a number for a grade: ")

# using (.isdigit) to make sure input is a number  
while not num.isdigit():

    # if input is not a number 
    num = input("You must enter a number: ")
 
 # input is a number 
else:
    num = int(num)



def check_grade(grade):
    if (num < 59):
        return "F"
    elif(59<num<65):
        return "D-"
    elif(64<num<70):
        return "D+"
    elif(69<num<75):
        return "C-"
    elif(74<num<80):
        return "C+"
    elif(79<num<85):
        return "B-"
    elif(84<num<90):
        return "B+"
    elif(89<num<95):
        return "A-"
    else:
        return "A+"
num_grade = check_grade(num)


print(f"A {num} is a {num_grade}")