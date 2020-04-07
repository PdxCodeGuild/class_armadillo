another_score = True
while another_score:

    score = int(input('Enter a numerical score between 0-100 to convert it to a letter grade: '))
    if score >= 100:
        print('A'+'+')
    if score >= 90 and score <= 99:
        if score % 10 <= 3:
            print('A' + '-')
        elif score % 10 >= 7:
            print('A' + '+')  
        else:
            print('A') 

    elif score >= 80 and score <= 89:
        if score % 10 <= 3:
            print('B' + '-')
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
        print('F, come see me')    

    calc = input('Would you like to convert another score to a letter grade? yes/no ')  
    if calc == 'no':
        print('Have a great day!')
        break                 

