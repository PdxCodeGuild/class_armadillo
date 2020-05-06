class Node:
    def __init__(self, element, next_elem=None):
        self.element = element
        self.next_elem = next_elem

    def __str__(self):
        return f'({self.element}, {self.next_elem})'

class Stack:
    def __init__(self):
        self.root = None
        self.node_count = 0
        self.nodes = []

    def is_empty(self):
        return not self.root

    def push(self, element):
        n = Node(element)
        n.next_elem = self.root
        self.root = n
        self.node_count += 1
        self.nodes.append(n.element)

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        popped = self.root
        self.root = self.root.next_elem
        return popped

    def peek(self):
        return self.root

    def length(self):
        return self.node_count

    def __str__(self):
        return 

def display_menu(choices):
    '''Prints out all available stack operations'''

    print()
    for num, choice in choices.items():
        print(f'{num}. {choice}')


choices = {
    '1': 'View the top item',
    '2': 'Add an item',
    '3': 'Remove the top item',
    '4': 'Display the total number of items',
    '5': 'Exit',
}

stack = Stack()

print("\nLet's get stackin'!")
print('-'*19)
while True:
    display_menu(choices)

    choice = input("\nEnter the number of the operation you'd like to perform: ")
    while choice not in choices:
        print('You must select a valid option:')
        choice = input("Enter the number of the operation you'd like to perform: ")

    if choice == '1':
        item = stack.peek()
        if item:
            print(f"The top item of the stack is: {item.element}")
        else:
            print("The stack is currently empty.")
    elif choice == '2':
        entry = input('Enter a number: ')
        while not entry.isnumeric():
            print('Please enter a number')
            entry = input('Enter a number: ')
        stack.push(entry)
    elif choice == '3':
        popped = stack.pop()
        print(f'{popped.element} was removed from the top of the stack.')
        print(f"Stack: bottom {' -> '.join(stack.nodes[::-1])} top")
    elif choice == '4':
        msg = 'is empty' if stack.is_empty() else f'has {stack.length()} items in it.'
        print(f'Your stack {msg}.')
        print(f"Stack: bottom {' -> '.join(stack.nodes[::-1])} top")
    elif choice == '6':
        print("Great stackin'! See you next time!")

