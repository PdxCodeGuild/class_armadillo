import random





eyes = [":", ";", "8", "B"]

noses = ["-", "~", "*"]

mouths = [")", "]", "/", "P"]

for i in range(1):
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print(f"{eye} {nose} {mouth}")