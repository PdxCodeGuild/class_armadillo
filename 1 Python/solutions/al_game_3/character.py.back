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
        self.inventory = []
        self.inventory_str = ''
        self.row_count = 1

    def inv_out(self):
        return str(self.inventory)

    def inv_update(self):
        self.inventory = sorted(self.inventory, key=str)
        invstr = 'inventory: '
        index_count = 1
        inv_count = 1
        holding_index = False
        row_count = 1
        for i in range(0, len(self.inventory)):
            if i == len(self.inventory) - 1:
                if holding_index:
                    invstr += str(self.inventory[i]) + '[' + str(index_count) + ']'
                    inv_count = 0
                else:
                    invstr += str(self.inventory[i])
                    inv_count = 0
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
        
