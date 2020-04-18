import string

#rotating by building up a dictionary
def rotn(text, n):

    
    alphabet = string.ascii_letters
    rot_alphabet = alphabet[n:] + alphabet[:n]
    # print(alphabet)

    dict1 = ""
    for letter in dict1:
        index = alphabet.index(letter)
        dict1 += rot_alphabet[index]
    return dict1
        
    # while index >= len(letter)
    #     dict1 -= len(dict2)



n = int(input("what is your rotation amount"))
print(rotn(text, n))





# Dictionary to lookup the index of alphabets 

# dictionary1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 
#         'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 
#         'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 
#         'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 
#         'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26} 


# # Dictionary to lookup alphabets  
# # corresponding to the index after shift 

# dictionary2 = {0 : 'N', 1 : 'O', 2 : 'P', 3 : 'Q', 4 : 'R', 5 : 'S', 
#         6 : 'T', 7 : 'U', 8 : 'V', 9 : 'W', 10 : 'X', 
#         11 : 'Y', 12 : 'Z', 13 :'A', 14 : 'B', 15 : 'C', 
#         16 : 'D', 17 : 'E', 18 : 'F', 19 : 'G', 20 : 'H', 
#         21 : 'I', 22 : 'J', 23 : 'K', 24 : 'L', 25 : 'M'}



#Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
#English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
#ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


#Allow the user to input the amount of rotation used in the 
#encryption. (ROTN)
#Version 2