# This example shows how to use an index value in a list
# to refer to the elements on either side of that value in the list

fruits = ['mango', 'peach', 'durian', 'squash', 'plum', 'boisenberry',  'strawberry']

print(f"{fruits =  }")

i = 1 # start at 0 go to 6, but if 'i=1' then it starts at 'peach'
while i < len(fruits) - 1:  # len(fruits) - 1 only goes to index 5

    print(f"{i = }")
    print(f"{fruits[i] = }")    # i is the current index in the list
    
    print(f"{fruits[i+1] = }")  # i + 1 refers to the next index in the list
    
    print(f"{fruits[i-1] = }")  # i - 1 refers to the previous index in the list



    i += 1 