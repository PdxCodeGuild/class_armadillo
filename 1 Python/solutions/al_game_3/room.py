import item
from random import randint, choice
class Coord():
    def __init__(self, in_coord, item=None):
        # Every set of coordinates has 3 points on the z-axis to place
        # items. It also has a status.
        # {{
        self.coord = in_coord
        self.z0 = item
        self.z1 = None
        self.z2 = None
        self.status = None
        # }}

    def __str__(self):
        return str(self.coord)

    def fall(self):
        # Checks if the space has an item in it. If the 3 z coordinates
        # aren't empty
        # {{
        has_item = False
        if not (self.z0 == None and self.z1 == None and self.z2 == None):
            has_item = True
        # }}
        if has_item:
            # Checks if there's space below to fall. If there's space
            # at the bottom, or space in the middle with something on top
            # {{
            space_below = False
            if self.z0 == None:
                space_below = True
            elif self.z1 == None and self.z2 != None:
                space_below = True
            # }}
            if space_below:
                # If there's only an item at the top, moves it to the bottom
                # {{
                if (self.z0 == None and self.z1 == None and self.z2 != None):
                    self.z0 = self.z2
                    self.z2 = None
                # }}
                # If objects can fall down one space, they do
                # {{
                else:
                    if self.z0 == None and self.z1 != None:
                        self.z0 = self.z1
                        self.z1 = None
                    if self.z1 == None and self.z2 != None:
                        self.z1 = self.z2
                        self.z2 = None
                # }}

    def place(self, item_in):
        # Place something on top of the lowest level of coordinates
        # available. Doesn't work if there's space below occupied z-coords
        # {{
        if self.z0 != None:
            if self.z1 != None:
                if self.z2 != None:
                    print("This space is occupied")
                else:
                    self.z2 = item_in
            else:
                self.z1 = item_in
        else:
            self.z0 = item_in
        # }}

    def announce(self):
        # This will print the stack on a space. First it checks if the
        # space is empty. If it isn't, it builds a list of objects
        # that exist on the space. It adjusts the output based on how many
        # objects are on the space.
        # {{
        if self.z0 == None and self.z1 == None and self.z2 == None:
            return "The space is empty."
        else:
            not_empty = []
            for i in [self.z0, self.z1, self.z2]:
                if i != None:
                    not_empty.append(i)
            if len(not_empty) == 3:
                return "The {} is on the {}, which is on the {}.".format(not_empty[2], not_empty[1], not_empty[0])
            elif len(not_empty) == 2:
                return "The {} is on the {}.".format(not_empty[1], not_empty[0])
            else:
                return "The {} is on the ground.".format(not_empty[0])
        # }}

    def take(self, myitem):
        # Take the item from it's z-coordinate, and
        # let everything else fall one space
        # {{
        if str(z0) == myitem:
            returnie = z0
            z0 = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z1) == myitem:
            returnie = z1
            z1 = z2
            z2 = None
            return returnie
        elif str(z2) == myitem:
            returnie = z2
            z2 = None
            return returnie
        # }}

    def take_z0(self):
        returnie = self.z0
        self.z0 = self.z1
        self.z1 = self.z2
        self.z2 = None

    def update():
        pass

# This creates a room with 25 by 25 coordinate objects, and then it randomly places
# barrels and boxes in the room. It also assigns the room one map coordinate
# {{
class Room():
    def __init__(self, characters, map_coord):
        self.characters = characters
        self.map_coord = map_coord
        self.coord_dict = {}

        for i in range(0, 25):
            for j in range(0, 25):
                self.coord_dict[(i, j)] = Coord((i, j))

        random_count = randint(0, 100)
        furniture_list = ['barrel', 'box']
        while random_count < 150:
            in_item = item.Furniture(choice(furniture_list))
            self.coord_dict[(randint(0, 24), randint(0, 24))].place(in_item)
            random_count += 1
    def __str__(self):
        return str(self.map_coord)

    def __repr__(self):
        return str(self.map_coord)

    def update_characters(self, characters):
        self.characters = list(characters)

    
# }
























































