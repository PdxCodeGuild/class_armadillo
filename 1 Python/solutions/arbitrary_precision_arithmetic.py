



class BigInt:
    def __init__(self, num):
        if type(num) is str or type(num) is int:
            self.num = [int(digit) for digit in str(num)]
        else:
            self.num = num

    def __str__(self):
        return ''.join([str(digit) for digit in self.num])

    def __eq__(self, other):
        return self.num == other.num

    def trim_leading_zeroes(self):
        while len(self.num) != 0 and self.num[0] == 0:
            self.num.pop(0)

        # for i in range(len(self.nums)):
        #     if self.nums[i] != 0:
        #         break
        # self.nums = self.nums[i:]


    def __add__(self, other):
        a = self.num
        b = other.num
        if len(a) < len(b):
            a, b = b, a
        b = [0] * (len(a) - len(b)) + b
        c = []
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            t = a[i] + b[i] + carry
            ones_digit = t % 10
            carry = t // 10
            c.insert(0, ones_digit)
        if carry == 1:
            c.insert(0, carry)
        return BigInt(c)

    def __mul__(self, other):
        if type(other) is int:
            c = BigInt(0)
            for i in range(other):
                c += self
            return c



if __name__ == '__main__':

    a = BigInt('00000')
    print(a.num)
    a.trim_leading_zeroes()
    print(a.num)
    exit()

    import random
    for i in range(10):
        a = [random.randint(0, 9) for j in range(random.randint(1,100))]
        b = [random.randint(0, 9) for j in range(random.randint(1,100))]
        a = BigInt(a)
        b = BigInt(b)
        c = a + b
        print(f'{a}\n+ {b}\n= {c}')
        print()


