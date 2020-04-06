

class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):  # returns the account balance
        return self.balance

    def deposit(self, amount):  # deposits the given amount in the account
        self.balance += amount
        self.transactions.append(f'user deposited ${amount}')

    def check_withdrawal(self, amount):  # returns true if the withdrawn amount won't put the account in the negative
        return amount < self.balance

    def withdraw(self, amount):  # withdraws the amount from the account and returns it
        self.balance -= amount
        self.transactions.append(f'user withdrew ${amount}')
        return amount

    def calc_interest(self):  # returns the amount of interest calculated on the account
        self.transactions.append(f'user gained interest ${self.balance * self.interest_rate}')
        self.balance += self.balance * self.interest_rate
        return self.balance

    def print_transactions(self):
        print('\n'.join(self.transactions))



# atm = ATM()
# atm = ATM(1000, 0.1)
# atm = ATM(balance=5000, interest=100)

# atm = ATM()
# print(atm.check_balance())  # "your balance is $0"
# atm.deposit(5)
# print(atm.check_balance())  # "your balance is $5"
# print(atm.check_withdrawal(10))  # False
# print(atm.withdraw(2))  # 2
# print(atm.check_balance())  # "your balance is $3"
# atm.print_transactions()

# > what would you like to do (deposit, withdraw, check balance, history)?
# > deposit
# > how much would you like to deposit?
# > $5
# > what would you like to do (deposit, withdraw, check balance, history)?
# > check balance
# > balance: $5


atm = ATM()

while True:
    command = input('what would you like to do (deposit, withdraw, check balance, history, exit)? ').lower()
    if command in ['done', 'exit', 'quit']:
        print('goodbye!')
        break
    elif command == 'deposit':
        amount = float(input('what is the amount you\'d like to deposit? '))
        atm.deposit(amount)
    elif command == 'withdraw':
        amount = float(input('what is the amount you\'d like to withdraw? '))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)
        else:
            print('You cannot withdraw more than you have!')
    elif command == 'check balance':
        print(f'Your account balance is ${atm.check_balance()}')
    elif command == 'history':
        atm.print_transactions()


