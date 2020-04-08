import random 


eyes = ["0  0", "o  o", "^  ^",]
noses = [" o", "  |", "  +"]
mouths = [" __ ", "  u", "#####"]
answer = input("would you like to see 5 faces? ")
while answer == 'yes':
    for face in range(5):
        eye = random.choice(eyes)
        nose = random.choice(noses)
        mouth = random.choice(mouths)
        print(f"{eye}\n{nose}\n{mouth}")
    answer = input("would you like to see 5 faces? ")
    if answer == "no":
        print("well..bye then")





