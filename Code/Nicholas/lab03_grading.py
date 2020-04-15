# this lab converts a numerical score to a letter grade:

another_score = True  #while loop allows user to enter more scores
while another_score:

    score = int(input('Enter a numerical score between 0-100 to convert it to a letter grade: '))  #gets user score in integer
    if score >= 100:  
        print('A'+'+')  #string concatenation to make grade + or -
    if score >= 90 and score <= 99:
        if score % 10 <= 3:  #use modulus to determine if grade is a minus or plus
            print('A' + '-')
        elif score % 10 >= 7:
            print('A' + '+')  
        else:
            print('A')  #if tenths place of grade is between 4-6, then A, no + or -

    elif score >= 80 and score <= 89:
        if score % 10 <= 3:  #use modulus to determine if grade is a minus or plus
            print('B' + '-')  #string concatenation to make grade + or -
        elif score % 10 >= 7:
            print('B' + '+')  
        else:
            print('B') 

    elif score >= 70 and score <= 79:
        if score % 10 <= 3:
            print('C' + '-')
        elif score % 10 >= 7:
            print('C' + '+')  
        else:
            print('C') 

    elif score >= 60 and score <= 69:
        if score % 10 <= 3:
            print('D' + '-')
        elif score % 10 >= 7:
            print('D' + '+')  
        else:
            print('D')         

    elif score <= 59:
        print('F, come see me')  #everything under 59 is F  
# asks user if they want to calculate another grade, if 'yes' then back to start of while loop
    calc = input('Would you like to convert another score to a letter grade? yes/no ')  
    if calc == 'no':  # if 'no' then prints the following and breaks:
        print('Have a great day!')
        break                 

