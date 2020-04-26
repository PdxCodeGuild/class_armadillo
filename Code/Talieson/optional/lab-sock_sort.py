import random


# These lists contain the possible sock attributes.
sock_types = ["ankle", "crew", "calf", "thigh"]
sock_colors = ["blue", "red", "green", "black", "white"]

# Sock pile is the list of starting socks, drawer is a dictionary post sort
sock_pile = []
sock_drawer = {}

# create 100 socks, each with a random color and type
for i in range(100):
    sock_pile.append((random.choice(sock_colors), random.choice(sock_types)))

# iterate over those socks, and build a dictionary with them
for sock in sock_pile:
    # if we have it in the dictionary, add 1 to it's value.
    if sock[0] + " " + sock[1] in sock_drawer:
        sock_drawer[sock[0] + " " + sock[1]] += 1
    # otherwise, add it to the dictionary with a value of 1
    else:
        sock_drawer.update({sock[0] + " " + sock[1]: 1})

# Now that their in the dictionary, find out how many pairs we have.
for sock in sock_drawer:
    # this gives us the number of pairs
    pairs = sock_drawer[sock] // 2
    # check if there is 1 or 2, so we don't have odd grammar later
    if sock_drawer[sock] == 1:
        print(f"Somehow I only have 1 {sock} sock?!")
    elif sock_drawer[sock] == 2:
        print(f"There is 1 pair of {sock} socks.")
    elif sock_drawer[sock] % 2 == 0:
        print(f"There are {pairs} pairs of {sock} socks.")
    else:
        print(f"There are {pairs} pairs of {sock} socks and 1 left over!")
