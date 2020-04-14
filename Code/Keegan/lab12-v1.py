

fruits = ['mango', 'peach', 'durian', 'squash', 'plum', 'boisenberry',  'strawberry']

print(f"{fruits =  }")

i = 1 # start at 0 go to 6, but if 'i=1' then it starts at 'peach'
while i < len(fruits) - 1:  # len(fruits) - 1 only goes to index 5

    print(f"{i = }")
    print(f"{fruits[i] = }")
    print(f"{fruits[i+1] = }")
    print(f"{fruits[i-1] = }")



    i += 1 