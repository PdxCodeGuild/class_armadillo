



def get_integer(message):
    while True:
        value = input(message)
        if value.isdigit():
            return int(value)
        else:
            print('that is not a valid integer')
    


def get_float(message):
    while True:
        value = input(message)
        try:
            value = float(value)
            return value
        except ValueError:
            print('that is not a valid float')
