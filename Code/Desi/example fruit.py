# colors = ["red", "purple", "green", "yellow"]


# main run loop
while True:
  # tested loop takes and validates input
  while True: 
    number = input("Enter a number to get a it's English translation.  If fininshed, enter done.  ")
    if number.isdigit():
      number = int(number)
      break
    elif number in ["done", "quit", "exit"]:
      print("Thanks for using numberst to English translation!   ")
      exit()
    else:   
        print("Enter a valid number between 0 - 999. ")
    hund_dig = number // 100
    ten_dig = (number - hund_dig*100)  // 10
    one_dig = number % 10
    if ten_dig == 1:
      output = f"{hundreds[hund_dig]} {tens[ten_dig]{one_dig}}"
    elif = hund_dig == 0 and ten_dig == 0 and one_dig == 0:
      output = "zero"
    else: 
      output = f"{hundreds[hund_dig]} {tens[ten_dig]{ones[one_dig]}"

    print(f"\n\t{number} in English is {output}!")

    