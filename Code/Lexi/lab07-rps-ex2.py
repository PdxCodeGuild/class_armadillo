import random
rps = ['r', 'p', 's']
computer_choice = random.randint(0, 2)
human_choice = input('r, p or s? ')
human_choice = rps.index(human_choice)
print(f'human chose     {rps[human_choice]}')
print(f'computer chose{rps[computer_choice]}')

# don't put it all on one line
#print('tie' if human_choice == computer_choice else 'human wins' if human_choice == (computer_choice))


if human_choice == computer_choice:
    print('tie')
elif human_choice == (computer_choice+1)%3:
    print('human wins')
else:
    print('computer wins')