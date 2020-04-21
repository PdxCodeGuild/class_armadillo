import random

# Talieson's challenge: have it all run within a loop to see when you
# can come out positive

# Find how many numbers match
# compare indexes
def num_matches(winning, ticket):
  #set up dictionary with winnings and matches
  matches = 0
  for i in range(6):
    if ticket[i] == winning[i]: # i will go 0,1,2,3,4,5
      matches += 1
  return matches
# print(num_matches([1,2,3,4,5,6],[1,2,3,4,5,6])) #hard code
# exit() # kills it



def pick_6():
  list_of_6 = []
  for i in range(6):
    list_of_6.append(random.randint(1, 99))
  return list_of_6
#print(pick_6())

expenses = 0
earnings = 0
balance = 0
play_count = 0
winners = pick_6()  # sets it equal to what we got above
print(winners) # [48, 93, 31, 91, 90, 43]

# Q: do you need to put quotes around keys?
# A: only if they are strings (these are INTs)
winnings = { 
  0 : 0, # dictionaries will crash if no key is valid
  1 : 4,
  2 : 7,
  3 : 100,
  4 : 50000,
  5 : 1000000,
  6 : 25000000,
}

# Matt's Q: where should we put the 'input' within the loop?
# so that every iteration of the loop, the user could receive the 
# balance and a message, "{balance} + Do you want to play again?"

while play_count < 100000: # <= will make it 11 times
  user = input(f"Your balance is: {balance} : Would you like to play again? y/n ")
  if user != 'y': # checking inverse condition
    print("Adios")
    break 

# Your balance is: 0 : Would you like to play again? y/n y
# Your balance is: -2 : Would you like to play again? y/n y
# Your balance is: -4 : Would you like to play again? y/n n
# Adios
# -4
# -1.0 

      
  
  # if user == 'y':
  #   continue # doesn't break the loop, it continues back to line 51
  # else:       #balance doesn't change
  #   print("Adios")


  play_count += 1
  # Subtract 2 from your balance (you bought a ticket)
  balance -= 2
  expenses -= 2
  #print(balance)
  #print(play_count) #looping 100,001 times
  # Generate a list of 6 random numbers representing the ticket
  ticket = pick_6()
  #print(ticket)

# balance += winnings[num_matches(winners, ticket)]
  matches = num_matches(winners, ticket)
  payout = winnings[matches]
  balance += payout
  earnings += payout



  # if matches > 2:
  #   print(winners)
  #   print(ticket)
  #   print(matches)
  #   print(payout)
  #   print(balance)
  #   print()


# [64, 56, 85, 65, 11, 71]
# [44, 49, 58, 71, 11, 56]
# 1
# 4
# -175502 file ch 13 bankruptcy

  # balance += winnings[num_matches(winners, ticket)]
  # taking the function, comparing it, return number of matching places,
  # updates balance with number from the dictionary


  # Q: does the first value in a dict need to be a string?
  # A: no, it has to be an immutable type... tuple...

print(balance)
print((earnings - expenses)/ expenses)
# [16, 20, 22, 33, 49, 30]
# -175606 poorer

# line 90 (version 2) (refer to line 51, 62)
# [60, 19, 94, 1, 96, 81]
# -176077
# -1.119615 for every dollar we invested, we lost $1.12 dolla billz