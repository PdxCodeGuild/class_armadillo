import random 

answer = ["it is certain", "It is decidedly so.", "Without a doubt.",
"Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely." "Outlook good.","Yes.", "Signs point to yes.", "Reply hazy,", "try again.", "Ask gain later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no." "Outlook not so good.", "Very doubtful."]



user = input("what is your name?: ")
 
print(input("Hello " + user + " what is your quuestion for the magic 8 ball?: "))

print(random.choice(answer))

while True:
    a = input("would you like to ask another question? yes or no:  ")
    if a == 'yes':
        input(f"okay {user} what is your question? ")
        print(random.choice(answer))
    elif a == "no":
        print(f"okay {user} have a nice day!")
        break
    else:
        print(f"sorry, {user} i dont understand that, " + a)






