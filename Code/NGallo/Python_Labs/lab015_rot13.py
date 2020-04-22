from string import ascii_lowercase

def rot13():
    user_input = str(input("Input a word to encrypt: "))
    user_value = int(input("Enter a number to scramble the word by: "))

    list_userinput = []
    # going into ascii list and finding index of the letter
    for letter in user_input:
        list_userinput.append(ascii_lowercase.index(letter))
    # rotates the index in the list
    new_index = [i + user_value for i in list_userinput]
   
    # starts the index over once you hit the end of the list
    rotated_index = [i%26 for i in new_index]

    # appends to final list the ascii string
    final_list = []
    for i in rotated_index:
        final_list.append(ascii_lowercase[i])

    # takes chars out of list and creates a string
    print_value = "".join(final_list)

    # print(list_userinput)
    # print(f"{new_index}")
    # print(f"{rotated_index}")
    print(print_value)
rot13()


'''
Lab 15: ROT Cipher
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