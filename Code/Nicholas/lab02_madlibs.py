#this lab takes various user inputs to create a madlib:

# Abraham Lincoln was the (number) 
# President of the (adjective) States.  He was
# over (number) feet tall and is known for 
# wearing a (adjective)(color) hat.
# Lincoln's (part of the body) is featured on the front of
# the penny and the (number) dollar bill.  Born
# in a (noun) cabin in Kentucky, Abraham 
# Lincoln grew up in (place).  He even became a (job) and went on to become 
# president. 

#initial greeting
print("Hello, let's play a madlib about the 16th president of the United States: " )

number1 = int(input("Pick a number, any number: "))  #these are all of the different inputs, this one asks for an integer
adj1 = input("Now give me an adjective: ") #this asks for a string
number2 = int(input("Pick another number, how about a big one? "))
adj2 = input("Give me another adjective: ")
color = input("Pick a color: ")
body_part = input("What's a random body part? ")
number3 = int(input("Give me another number: "))
noun = input("Let's have a noun: ")
place = input("What's the last place you visited for fun? ")
job = input("What was your least favorite job?: ")

while True:  #this while asks user if they would like to hear the madlib 
    play_story = input("Thanks for your input! Would you like to see the madlib? yes/no ")
    if play_story.lower() == "yes":
        print(f'Abraham Lincoln was the {number1}th President of the {adj1} States.')  #uses formatted strings to display mutiple user inputs in one string
        print(f'He was over {number2} feet tall and is known for wearing a {adj2} {color} hat.')
        print(f'Lincoln\'s {body_part} is featured on the front of the penny and the {number3} dollar bill.') 
        print(f'Born in a {noun} cabin in Kentucky, Abraham Lincoln grew up in {place}.')
        print(f'He even became a {job} and went on to become president.') 
    elif play_story.lower() == "no":  #if user selects no, then it ends and prints statement.
        print("Thanks for your input! Good bye!")  
        break  


