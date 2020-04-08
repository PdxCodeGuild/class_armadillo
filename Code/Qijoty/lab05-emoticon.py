#emoticon lab
'''

    Define a list of eyes
    Define a list of noses
    Define a list of mouths
    Randomly pick a set of eyes
    Randomly pick a nose
    Randomly pick a mouth
    Assemble and display the emoticon
    make the emoticon display the emotion of the user
    generate horizontal or vertical
'''
i = 0
while i < 1:
    import random

    eyes = [':', ';', 'x', '8']
    nose = ['-','.', 'v', '^', '*', '@']
    mouth = ['3', '>', ')', '$', 'o']

    emotion = input('Are you feeling happy, sad, angry or something else today? ')

    if emotion == "happy":
        print(':-)))')
    elif emotion == "sad":
        print(':-[[[')
    elif emotion == "angry":
        print('>:{\{\{')
    else:
        print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))

    while True:
        user_input = input("would you like another emoticon? ").lower()
        if user_input == "yes":
            print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))
        else:
            print('okie dokie, byeee')
    '''
    for emoticon in range(5):
        face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
        print(face)
    '''


    face = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    print(face)
