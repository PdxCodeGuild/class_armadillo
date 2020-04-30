# lab 21
# ask user for input
user_input = int(input("What is the number you'd like? : "))

# make dictionary
dictionary = {
  10 : "teen",
  20 : 'twenty',
  30 : 'thirty',
  40 : 'forty',
  50 : 'fifty',
  60 : 'sixty',
  70 : 'seventy',
  80 : 'eighty',
  90 : 'ninety',
}

# make a function to deal with ones 
def if_ones(user_input):

  return(user_input)

# make a function to deal with tens
def tens(user_input):

  return(user_input)

# BELOW ARE GLOBAL VARS

# test printing out what the user input
first_part = (dictionary[user_input])
print(first_part)

# 
# extract ones digit
tens_digit = user_input//10
print(tens_digit)

ones_digit = user_input%10
print(ones_digit)
