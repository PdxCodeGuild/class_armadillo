
cc = '4556737586899855'
cc = [int(d) for d in cc]
check_digit = cc.pop()
# cc.reverse()
# cc = cc[::-1]
cc = [cc[len(cc)-i-1] for i in range(len(cc))]
cc = [2*cc[i] if i%2 == 0 else cc[i] for i in range(len(cc))]
cc = [d-9 if d > 9 else d for d in cc]
if check_digit == sum(cc) % 10:
    print('valid')

