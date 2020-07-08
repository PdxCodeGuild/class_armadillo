test_types = [bool, int, float, str, dict]

values = [None, True, False, 0, 1, 0.0, 1.0]


for value in values:
    for test_type in test_types:
        print(f'{type(value)}\t{value}\t->\t{test_type}\t', end='')
        try:
            print(test_type(value))
        except:
            print('error')


