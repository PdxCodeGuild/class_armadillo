# lab 21 - converts numerics to english


ones = {
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
        0 : "zero",
}
# make dictionary
tens_dict = {
  10 : "teen",
  20 : 'twenty',
  30 : 'thirty',
  40 : 'forty',
  50 : 'fifty',
  60 : 'sixty',
  70 : 'seventy',
  80 : 'eighty',
  90 : 'ninety',
  0  : 'zero',
}

hundreds = {1: "one hundred", 2: "two hundred", 3: "three hundred",
            4: "four hundred", 5: "five hundred", 6: "six hundred",
            7: "seven hundred", 8: "eight hundred",
            9: "nine hundred", 0: ""}

# main run loop
while True:
  # test input

  number = int(input("Enter a numeric value 0 - 999: "))


  print(number)
  # floor divide hundreds
  hundreds_place = (number // 100)
  print(hundreds_place)
  # floor divide minus first index/hundreds' place to get tens' place
  tens_place = ((number) // 10)
  print(tens_place)
  # use modulo to get ones' place
  ones_place = (number % 10)
  print(ones_place)
  # check if we have a remainder in the tens' place
  if tens_place == 1:
    result = f'{hundreds[hundreds_place]} { tens_dict[tens_place][ones_place]}'
  elif hundreds_place == 0 and tens_place == 0 and ones_place == 0:
    result = "zero"

  else:
    result = f'{hundreds[hundreds_place]} {tens_dict[tens_place]} {ones[ones_place]}'
  
  print(result)

 # line 55, in <module>
#     result = f'{hundreds[hundreds_place]} { tens_dict[tens_place][ones_place]}'
# KeyError: 1