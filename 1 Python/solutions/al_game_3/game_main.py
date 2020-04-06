import room, item, curses
from time import sleep
from random import randint
import character

# This will look up the visual character representation based on the
# inputed item's name
# {{
def get_visual_character(item):
    visual_char_dict = {'barrel': '🛢', 'box': '☐', 'Melgas': '👵', 'door': '🚪'}
    return visual_char_dict[item.name]
# }}


# This function prints the room to the screen. It checks the z0 value
# of every room coordinate (which is whatever is on the floor), and
# if there's nothing there then it will print a period. Otherwise it
# uses the get_visual_character() function to figure out what to place
# in the coordinates, based on the z0 item's name.
# All coordinates are shifted so that the x-axis is doubled in length,
# because otherwise it would look compressed.
# {{
def print_room(in_room, the_player):
    for (i, j) in in_room.coord_dict:
        if in_room.coord_dict[(i, j)].z0 == None:
            try:
                myscreen.addstr(i, j * 2, '.')
            except:
                pass
        else:
            visual_char = in_room.coord_dict[(i, j)].z0
            myscreen.addstr(i, j * 2, get_visual_character(visual_char))
    myscreen.addstr(the_player.location[0], the_player.location[1] * 2, get_visual_character(the_player))# }}

# This allows you to place an item with map coordinates. It takes in
# the room and coordinates, and it accesses the Coord object based on that
# information. The Coord object has a "place" method that this function
# uses.
# {{
def place_with_map_coords(in_room, in_item, in_coords):
    in_room.coord_dict[(in_coords[0], in_coords[1])].place(in_item)
# }}

def check_win(player):
    pass
        
def check_death(player):
    pass

def update_player(player):
    check_win(player)
    check_death(player)

def update_characters(characters):
    for i in characters:
        if i.health < 0:
            pass #kill them here
    pass

def update_room(in_room):
    for i in in_room.room_coord:
        i.update

def update(player, in_room, characters):
    update_player(player)
    update_characters(characters)
    update_room(in_room)

players = []
rooms = []

# The game is not over, and the player has not yet done anything to use up
# their turn
# {{
game_over = False
turn_finished = False
# }}

# Establish a screen
# {{
myscreen = curses.initscr()
# }}

# Make a test player
# {{
test_player = character.Player()
# }}

# Make a dictionary of rooms
# {{
main_room_dict = {}
for i in range(0, 5):
    for j in range(0, 5):
        main_room_dict[(i, j)] = room.Room([], (i, j))
# }}

main_room_dict[(0, 0)].characters.append(test_player)
print_room(main_room_dict[(0, 0)], test_player)

# Place test items at (24, 10)
# {{
for i in range(0, 3):
    furniture_list = ['box', 'box', 'barrel']
    main_room_dict[(0, 0)].coord_dict[(24, 10)].place(item.Furniture(furniture_list[i]))
# }}

# Run the while loop, and react to different inputs

myscreen.keypad(True)
while game_over == False:
    myscreen.clear()

    # Print the screen, what items exist on the floor at the player's position,
    # and the player's inventory
    # {{
    print_room(main_room_dict[(0, 0)], test_player)
    myscreen.addstr(26, 0, main_room_dict[(0, 0)].coord_dict[test_player.location].announce())
    myscreen.addstr(27, 0, test_player.inventory_str)
    control_string = '----------------------------\n' + \
    'Press up, down, left, right\n' + \
    "Press 't' to take an item\n" + \
    "Press 'q' to quit"
    myscreen.addstr(27 + test_player.row_count, 0, control_string)
    inkey = myscreen.getkey()
    # }}

    # Movement
    # {{
    if inkey == 'KEY_UP':
        new_loc = (test_player.location[0] - 1, test_player.location[1])
        if new_loc in main_room_dict[(0, 0)].coord_dict:
            test_player.location = new_loc
    elif inkey == 'KEY_DOWN':
        new_loc = (test_player.location[0] + 1, test_player.location[1])
        if new_loc in main_room_dict[(0, 0)].coord_dict:
            test_player.location = new_loc
    elif inkey == 'KEY_RIGHT':
        new_loc = (test_player.location[0], test_player.location[1] + 1)
        if new_loc in main_room_dict[(0, 0)].coord_dict:
            test_player.location = new_loc
    elif inkey == 'KEY_LEFT':
        new_loc = (test_player.location[0], test_player.location[1] - 1)
        if new_loc in main_room_dict[(0, 0)].coord_dict:
            test_player.location = new_loc
    # }}

    # If you press 't' then take what's at z0, and let everything else fall
    # {{
    elif inkey == 't':
        if main_room_dict[(0, 0)].coord_dict[test_player.location].z0 != None:
            test_player.inventory.append(main_room_dict[(0, 0)].coord_dict[test_player.location].z0)
            test_player.inv_update()
            main_room_dict[(0, 0)].coord_dict[test_player.location].z0 = None
            main_room_dict[(0, 0)].coord_dict[test_player.location].fall()
    # }}

    elif inkey == 'q':
        game_over = True

    # If you're standing on a box, and there's something in the box, automatically take it
    # {{
    if main_room_dict[(0, 0)].coord_dict[test_player.location].z0 != None:
        if main_room_dict[(0, 0)].coord_dict[test_player.location].z0.name == 'box':
            if main_room_dict[(0, 0)].coord_dict[test_player.location].z0.has != None:
                test_player.inventory.append(main_room_dict[(0, 0)].coord_dict[test_player.location].z0.has)
                test_player.inv_update()
                main_room_dict[(0, 0)].coord_dict[test_player.location].z0.has = None
    # }}

curses.endwin()
# }}
            
    












































