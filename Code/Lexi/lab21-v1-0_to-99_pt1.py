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

# append values
# edge cases, hard coding, using functions
first_part = (dictionary[user_input])
print(first_part)



# make it go from 0 to 99

# 
# extract ones digit
tens_digit = user_input//10
print(tens_digit)

ones_digit = user_input%10
print(ones_digit)


# IF I TYPE IN 89 - FAIL (SEE BELOW)
#   first_part = (dictionary[user_input]) KeyError: 89

# IF I TYPE IN 20 - SUCCESS(SEE BELOW)
# What is the number you'd like? : 20
# twenty
# 2
# 0