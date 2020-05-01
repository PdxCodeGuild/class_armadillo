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

hundreds = {1: "one hundred and", 2: "two hundred and", 3: "three hundred and",
            4: "four hundred and", 5: "five hundred and", 6: "six hundred and",
            7: "seven hundred and", 8: "eight hundred and",
            9: "nine hundred and", 0: ""}

# main run loop
while True:
  # test input


  # if number.isdigit():
  #   number = int(number)
  #   break < - Jon said this is my problem
  # # elif number in ['done']:
  #   print("Thanks for using this code")
  
  number = int(input("Enter a numeric value 0 - 999: "))
  # floor divide hundreds
  hundreds_place = number // 100
  # floor divide minus first index/hundreds' place to get tens' place
  tens_place = (number - hundreds*100)// 10
  # use modulo to get ones' place
  ones_place = number % 10
  # check if we have a remainder in the tens' place
  if tens_place == 1:
    result = f'{hundreds[hundreds_place]} { tens_dict[tens_place][ones_place]}'
  elif hundreds_place == 0 and tens_place == 0 and ones_place == 0:
    result = "zero"

  else:
    result = f'{hundreds[hundreds_place]} {tens_dict[tens_place]} {ones[ones_place]}'
  
  print(result)

  '''So if you print out number anywhere after line 40-44 is doesn't do anything.

If you print right after 39
it does work

if you comment line 40-44 it then prints out everything

I would ask for input at the end of the result and use line 43-44 to ask whether or not they want to continue with the loop, otherwise break

Oh also on line 42 you added break

That breaks out of the while loop and won't print anything. I think that's the main culprit

breaks will break which ever loop it is currently in

line 40-41 are not needed because you can simply wrap int() around the input

It will always be a number'''