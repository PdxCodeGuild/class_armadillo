"""---------------------------------Practice Strings---------------------------------"""












































# # Problem 1
# # Get a string from the user, print out another string, doubling every letter.

def double_letters(word):
    return ''.join([i*2 for i in word])
    
# print(double_letters('bubbles'))

# #Problem 5 (not from strings)

def reverse(nums):
    nums.reverse()
    return nums

mylist = [1, 2, 3] 
# print(reverse(mylist))

# # Problem 2
# # Write a function that takes a string, and returns a list of strings, each missing a 
# # different character.

# def missing_char(word): # need to break up the string and populate the list
    strings_list = [] # heres the list
    for char in word: # need a loop that sends each letter at the position of i to stringslist
        strings_list.append(char)
        print(char)
    print(strings_list)
    return word

# print(missing_char('kitten')) # ['itten', 'ktten', 'kiten', 'kiten', 'kittn', 'kitte']

# #operations
# print(5/2) # division (5/2=2.5)

# print(5//2) # floor division drops the remainder

# print(5%2)  # modulus returns just the remainder

# print(len('hello world'))

# s = 'hello world'
# print(s[6])
# print(s[3:9])
# print(s[0])

# print('hello world it\'s a great day'.replace('h', 'hh'))


# personal challenge - make 1 min timer..
import time

def sixty_seconds():
    second = 60
    while second >= 1:
        time.sleep(1)
        second -= 1
        print(second)
sixty_seconds()
        
