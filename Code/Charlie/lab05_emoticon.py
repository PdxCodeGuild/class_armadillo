import random




# variable eyes is = to a list that contains possible eyes
eyes = [":", ";", "8", "B"]
# variable noses is = to a list that contains possible noses
noses = ["-", "~", "*"]
# variable mouth is = to a list that contains possible mouths
mouths = [")", "]", "/", "P"]

for i in range(1):
    # variable eye = the random choice from the list (eyes)
    eye = random.choice(eyes)
    # variable nose = the random choice from the list (noses)
    nose = random.choice(noses)
    # variable mouth = the random choice from the list (mouths)
    mouth = random.choice(mouths)
    # this f string inputs the random choice for each variable 
    print(f"{eye} {nose} {mouth}")