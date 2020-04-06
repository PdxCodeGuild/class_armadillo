class Item:
    # Every item has a name, a type, and an attack value
    # {{
    def __init__(self, name, item_type, attack=2):
        self.name = name
        self.item_type = item_type
        self.attack = attack
    # }}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Spell(Item):
    # Every spell has a name, an attack value, and a status
    # it can apply to objects/players/coordinates
    # {{
    def __init__(self, name):
        param = {'fire spell': [50, 'on fire']}
        self.status_change = param[name][1]
        super().__init__(name, 'spell', param[name][0])
    # }}

    def __str__(self):
        return self.name

class Furniture(Item):
    # Furniture can have stuff in it. Still in alpha, so
    # I just put nothing in barrels and a fire spell in
    # boxes. Barrels and boxes also do 10 damage when thrown.
    # {{
    def __init__(self, name):
        self.box_in = None
        if name == 'box':
            self.box_in = Spell('fire spell')
        param = {'box': [10, self.box_in], 'barrel': [10, None]}
        super().__init__(name, 'furniture', param[name][0])
        self.has = param[name][1]
    # }}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Maker_maker(Item):
    # Makers are experimental funiture that make more items when placed. Not yet implemented. Love spell not yet implemented.
    # {{
    def __init__(self, name):
        param = {'maker maker': ['maker', 'Maker_maker'], 'barrel maker': ['barrel', 'Furniture'], 'love maker': ['love spell', 'Spell']}
        self.makes = param[name][0]
        self.makes_type = param[name][1]
        super().__init__(name, 'maker', 0)
    # }}

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
