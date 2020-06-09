



# Python program to implement  
# ROT13 Caesar cipher 
  
'''This script uses dictionaries instead of 'chr()' & 'ord()' function'''
  
# Dictionary to lookup the index of alphabets 

dictionary1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26} 


# Dictionary to lookup alphabets  
# corresponding to the index after shift 

dictionary2 = {0 : 'N', 1 : 'O', 2 : 'P', 3 : 'Q', 4 : 'R', 5 : 'S', 
        6 : 'T', 7 : 'U', 8 : 'V', 9 : 'W', 10 : 'X', 
        11 : 'Y', 12 : 'Z', 13 :'A', 14 : 'B', 15 : 'C', 
        16 : 'D', 17 : 'E', 18 : 'F', 19 : 'G', 20 : 'H', 
        21 : 'I', 22 : 'J', 23 : 'K', 24 : 'L', 25 : 'M'}


# phrase = input("Enter the letters you'd like to be encrypted: ")

# defines rot function.
def encrypt(message): 
    # creates string coe to iterate over to find indices
    cipher = 'abcdefghijklmnopqrstuvwxyz' 
    # creates open string so user can enter a code
    phrase = ''
    # initiates loop
    for letter in message: 
        # checking for space 
        if letter == ' ': 
            phrase += ' '
            # attaches user phrase using rot13 code 
        else: 
            phrase += cipher[(cipher.find(letter)+13)%26]
  
  # returns phrase from below
    return phrase
# users input of what they want encrypted.
message = input("Enter the letters you'd like to be encrypted: ")
# message2 = input("How many rotations of Rot13 would you like?  ")
# prints the encrypted msg.
print(f'Your new code is {encrypt(message)}')



    

#Lab 15: ROT Cipher
#Write a program that prompts the user for a string,
#and encodes it with ROT13. For each character, find
#the corresponding character, add it to an output
#string. Notice that there are 26 letters in the English 
#language, so encryption is the same as decryption.

#Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
#English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
#ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


#Allow the user to input the amount of rotation used in the 
#encryption. (ROTN)
#Version 2