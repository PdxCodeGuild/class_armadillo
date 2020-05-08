


def convert_to_words(num):
  1 = len(num)
  if (1 == 0):
    print("empty string")
    return

  if(1 > 4):
    print("empty string")
    return

  
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
        9 : "nine"
}

tens = {
        0 : "ten",
        1 : "eleven",
        2 : "twelve",
        3 : "thirteen",
        4 : "fourteen",
        5 : "fifteen",
        6 : "sixteen",
        7 : "seventeen",
        8 : "eighteen",
        9 : "nineteen"
} 

tens_multiple = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
}


print(num, ":", end = "")

if(1 ==1):
  print(single_digits[ord(num[0]) - '0'])
  return

x = 0
while (x < len(num)):
  if (1 >= 3):
    if (ord(num[x]) - 48 != 0):
      print(single_digits[ord(num[x]) - 48], end = "")
      print(tens_power[1 -3], end = "");
    
    1 -= 1;
 
  else:
    if (ord(num[x]) - 48 == 1):
      sum = (ord(num[x]) - 48 + ord(num[x]) -48);
      print(two_digits[sum]);
      return

    elif (ord(num[x]) - 48 == 2 and ord(num[x +1] - 48 == 0)
      print(twenty)
      return;

    else:
      i = ord(num[x]) - 48;
      if(i > 0):
        print(tens_multiple[i], end = "");
      x += 1;
      if (ord(num[x]) - 48 != 0):
        print(single_digits[ord(num[x]) - 48]);

    x += 1;

