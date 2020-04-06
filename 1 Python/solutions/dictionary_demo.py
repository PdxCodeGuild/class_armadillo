


product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}

print(product_to_price)


product_to_price['apple'] = 1.25  # replaces a value
product_to_price['banana'] = 1.25  # adds a key-value pair


# iterate over keys
for key in product_to_price:
    print(f'{key} {product_to_price[key]}')

# iterate over values
for value in product_to_price.values():
    print(f'{value}')

# print(list(product_to_price.values()))



# iterate over keys and values
for key, value in product_to_price.items():
    print(f'{key} {value}')






# rot 13

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# n = int(input('rotate by what amount? '))
#
# translate = {}
# for char in alphabet:
#     rotated_char = alphabet[(alphabet.index(char) + n)%len(alphabet)]
#     translate[char] = rotated_char
#
#
# word = input('what is the word?')
#
#
# output = ''
# for char in word:
#     if char in translate:
#         output += translate[char]
#     else:
#         output += char
#
# print(output)






product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}
while True:
    command = input('would you like to create, retrieve, update, delete or list? ')
    if command == 'create':
        key = input('what is the fruit? ')
        if key in product_to_price:
            print('that\'s already in there!')
            continue
        value = float(input('what is the price? '))
        product_to_price[key] = value

    elif command == 'list':
        for key in product_to_price:
            print(f'{key}: {product_to_price[key]}')















