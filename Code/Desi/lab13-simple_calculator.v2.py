#version 2 -DOES NOT WORKP- STICK WITH LAB 13 V1
pmName = input('Enter module name: /lab13-simple_calculator.v1/)
pm = __import__(pmName)
print(dir(pm))



play_again = input("Would you like to continue?: y/n ")
        
if play_again == "y":
  while True:
    choice = input("Which operation would you like to perform: ")
    if choice == "done":
      print("Ciao!")
      exit()
                    
    num_3 = input("Choose a number: ")
  if num_3 == "done":
    print("Asta la vista!")
    exit()
                
    num_3 = float(third_num)
  if o == "+":
    answer = answer + num_3
    print(f"\n{answer} {choice} {num_3} = {answer} ")

  elif choice == "-":
    answer = answer - num_3
    print(f"\n{answer} {choice} {num_3} = {answer} ")

  elif choice == "/":
    answer = answer / num_3
    print(f"\n{answer} {choice} {num_3} = {answer} ")

  elif choice == "*":
    answer = answer * num_3
    print(f"\n{answer} {choice} {num_3} = {answer} ")
                
  else: 
    print("Please try again... ")   
        
