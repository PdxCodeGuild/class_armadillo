import random
# mistake: put break within the if-else
# Talieson helped me understand to line it up with the if-else
# in order to be outside so that once one of the if-else lines were
# run, then the program would exit the loop - SUCCESS
# generating a random number

num = random.randint(0, 9)
dictionary = {
        0 : "zero",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
}

# # while True loop to take user input
# while True:
#     # ask the user to enter digits
#     user = input("Please enter digit 0 - 9: ")
#     if user in ["done", "quit", "exit"]:
#         break
#     else:
#         print("Not a valid entry.")


while True:
  if num == 0:
    print(dictionary[0])
  elif num == 1:
    print(dictionary[1])
  elif num == 2:
    print(dictionary[2])
  elif num == 3:
    print(dictionary[3])
  elif num == 4:
    print(dictionary[4])
  elif num == 5:
    print(dictionary[5])
  elif num == 6:
    print(dictionary[6])
  elif num == 7:
    print(dictionary[7])
  elif num == 8:
    print(dictionary[8])
  elif num == 9:
    print(dictionary[9])
  else:
    exit()
  break