# Convert a given number into its English representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

# Cover cases 0-9 first, then 10-19, then 20-99

seed_number = int(input('Enter a Number from 0-9: '))



x = 67
tens_digit = x//10
ones_digit = x%10

# print(seed_number)

ones = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',

    }
tens = {
    2: 'twenty',
    3: 'thirty',
}
def english(seed_number):
    if seed_number == 1:
        print('One')

print(english(seed_number))