import item
class Character:
    def __init__(self, name, location, health = 100):
        self.location = location
        self.name = name
        self.health = health

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Player(Character):
    def __init__(self):
        super().__init__('Melgas', (24, 12), 500)
        # The inventory is empty, the string representation of
        # the inventory is empty, and the number of rows the inventory
        # takes up is one
        # {{
        self.inventory = []
        self.inventory_str = ''
        self.row_count = 1
        # }}

    def inv_update(self):
        # Sort the inventory alphabetically
        # {{
        self.inventory = sorted(self.inventory, key=str)
        # }}
        # Create a string to represent the inventory
        # invstr is the string that is concatenated to become
        # the inventory that displays on the screen
        # index_count counts how many of each item
        # inv_count is to make sure that the string representation
        # has a maximum length
        # holding_index means that you have more than one item, and
        # need to add the number to that string
        # row_count keeps track of the size of the string, so it can
        # be displayed properly
        # {{
        invstr = 'inventory: '
        index_count = 1
        inv_count = 1
        holding_index = False
        row_count = 1
        # }}
        # Build the inventory string
        # {{
        for i in range(0, len(self.inventory)):
            # If this is the last item in the inventory,
            # don't run code that looks for the next item
            # {{
            if i == len(self.inventory) - 1:
                if holding_index:
                    invstr += str(self.inventory[i]) + '[' + str(index_count) + ']'
                    inv_count = 0
                else:
                    invstr += str(self.inventory[i])
                    inv_count = 0
            # }}
            # If [i] == [i + 1], then it's holding an index, which is 2 and
            # might go up
            elif str(self.inventory[i]) == str(self.inventory[i + 1]):
                holding_index = True
                index_count += 1
            else:
                if holding_index:
                    invstr += str(self.inventory[i]) + '[' + str(index_count) + '], '
                    index_count = 1
                    holding_index = False
                    inv_count += 1
                else:
                    invstr += str(self.inventory[i]) + ', '
                    inv_count += 1
            if inv_count > 1:
                inv_count = 0
                invstr += '\n'
                row_count += 1
        self.row_count = row_count
        self.inventory_str = invstr
        return None

                



















                        



























        
