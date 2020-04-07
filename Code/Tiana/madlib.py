import random


adjective = input('Give 3 adjectives separated by commas. ' )
newadj = adjective.split()
adj = list(newadj)
ran_adj = random.choice(adj) 


silly_word = input("Enter a silly word. ")
lname = input("Enter a last name. ")
illness = input("Enter a illness. ")
noun = input("Enter a noun. ")
silly_word2 = input("Enter another silly word. ")
place = input("Enter a place. ")
number = input("Enter a number. ")





madlib = (f"{silly_word} {lname} will not be attending school today. He/she has come down with a case of {illness} and has horrible {noun} sores and a {ran_adj} fever. We have made an appointment with the {ran_adj} Dr. {silly_word2} , who studied for many years in {place} and has {number} degrees in pediatrics. He will send you all the information you need. Thank you! Sincerely Mrs.{ran_adj}. ")

story = input('Would you like to hear the story? ')

while story == 'yes':
    print(madlib)
    print(story)
    break
while story == 'no':
    print('Alright :( . ')
    break