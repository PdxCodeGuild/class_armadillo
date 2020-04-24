import random
#step 1 
def pick6():
    winners = []
    for i in range(6):
        winners.append(random.randint(1, 99))
    return winners

def num_matches(winners, user_ticket):
    matches = 0
    for i in range(len(winners)):
        if winners[i] ==  user_ticket[0]:
            matches += 1     
    print(matches)
    return matches
print (f'Winning ticket: {pick6()}')    

#step 2
balance = 0
#step 3 
for i in range(100000):
    user_ticket = pick6()   
print(f'Your ticket: {user_ticket}')
# balance -= 2 

#step 5
# balance = 0 - 2












