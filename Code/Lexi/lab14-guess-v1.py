
import random
def guessing():

    while True:

        pc_guess = random.randint(1,10)
        # user guess
        user_guess = int(input("Guess a number 1-10: "))
        # compare both guesses
        if pc_guess > user_guess:
            print(f'pc wins')
        elif pc_guess < user_guess:
            print(r'user wins')
            print(r'(\____/)')
            print(r' ͡ ͡° ͜ ʖ ͡ ͡°')
            print(r'\╭☞ \╭☞')
        elif pc_guess == user_guess:
            print(f'tie')
        else:
            print("Try again, invalid entry")

        # output = print( f'User: \' {user_guess} \'pc:\'  {pc_guess} ')
        output = print(f' " User guess is "{user_guess} " PC guess is: " {pc_guess} " ') 
    return output
print(guessing())


# mistakes: not knowing where print and return go, raw vs formatted string

'''MY FIRST VERSION WITH MISTAKES BELOW

You just had some syntax errors if you want to compare them, other than works perfectly!

Also you weren't using a param and arguement for this function

You were saying the param was def g_pc_vs_me(int)

but not using it anywhere in the code, so you could just leave it blank like so

line 17 you were doing concatenating, but jsut left out the + signs on either
 side of the variables as well as the f

Otherwise you are on the right track! Now ya just need a loop


Line 18 also needed to be indented to be nested in the function

import random
def g_pc_vs_me(int):
    # computer will guess a random int between 1 and 10
    pc_guess = random.randint(1,10)
    # user guess
    user_guess = int(input("Guess a number 1-10"))
    # compare both guesses
    if pc_guess > user_guess:
        print(f'pc wins')
    elif pc_guess < user_guess:
        print(f'user wins')
    elif pc_guess == user_guess:
        print(f'tie')
    else:
        print("Try again, invalid entry")
    # output
output = print( 'User: ' {user_guess} 'pc: ' {pc_guess} )
    return output

    '''