import random 

print("\n\n-----Random Face Gen-----\n")
face_input = input("press any button to generate a face: ")

def make_a_face():

    loop = True

    while True:
        eye = [':', ';', '=', 'O',]

        nose = [">", "-"]

        mouth = ['D', ')', '(', '|', 'p',]

        random_eye = random.choice(eye)
        random_nose = random.choice(nose)
        random_mouth = random.choice(mouth)

        random_face = random_eye + random_nose + random_mouth

        print(f'\n{random_face}\n')

        try_again = input("would you like to make another face? y/n ")
        
        if try_again == "y":
            continue
        elif try_again == "n":
            print("Take it easy!")
            exit()
        else:
            print("\nI didn't understand that...\n ...here's another face to entertain you: ")

make_a_face()

