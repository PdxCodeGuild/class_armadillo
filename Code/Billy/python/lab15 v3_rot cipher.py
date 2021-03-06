# ascii method  (www.asciitable.com)
def rotn(text, num): # includes rotation input, negative number for reverse
    output = '' # makes empty output list
    for x in text: # iterates through input one character(chr)(char) at a time
        ascii_code = ord(x) # changes char to ascii
        if 97 <= ascii_code <= 122: # lower case
            ascii_code -= 97 # starts sequence at 0
            output += chr((ascii_code + num)%26 + 97) 
            # rotates, shifts, changes ascii to chr, adds to ouput variable 
        elif 65 <= ascii_code <= 90: # upper case
            ascii_code -= 65
            output += chr((ascii_code + num)%26 + 65)
        elif 32 <= ascii_code <= 64 or 91 <= ascii_code <= 96 or 123 <= ascii_code <= 126: 
            # space, numbers, special char groups (ascii special char are separated into four groups)
            output += chr(ascii_code) # no rotation required for these characters 
        else:
            output += chr(ascii_code)
            print(f'\n\'{x}\' is an invalid entry...cannot encrypt that character.') # input validation       
    return output

print(rotn('Hello2!^~', 14)) # Vszzc2!^~
# print(rotn('Vszzc2!^~', -14)) # Hello2!^~ --tests function









'''
Lab 15: ROT Cipher 12.18.27
Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)

Version 3 (optional)
Add support for capital letters, numbers, and special characters. These can be handled in two different ways:

Capital letters can be rotated as well, numbers and special characters can be put directly into the output (e.g. "hello world!" becomes "uryyb jbeyq!").

Instead of using an alphabet of just letters, include numbers, spaces, and special characters as well.
'''