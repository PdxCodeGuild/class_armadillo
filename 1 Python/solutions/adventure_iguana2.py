

import random

class Entity:
    def __init__(self, i, j, icon):
        self.i = i
        self.j = j
        self.icon = icon


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def get_entities(self, i, j):
        r = []
        for entity in self.entities:
            if entity.i == i and entity.j == j:
                r.append(entity)
        return r

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                for entity in self.entities: # find an entity at this i,j to draw
                    if entity.i == i and entity.j == j:
                        print(entity.icon, end='')
                        break
                else:
                    print(' ', end='')
            print()



def main():
    world = World(10, 10)
    player = Entity(2, 2, '☺')
    world.entities.append(player)
    for i in range(5):
        enemy_i, enemy_j = world.random_location()
        while len(world.get_entities(enemy_i, enemy_j)) != 0:
            enemy_i, enemy_j = world.random_location()
        enemy = Entity(enemy_i, enemy_j, '§')
        world.entities.append(enemy)


    while True:
        world.print()
        command = input('what is your command? ')  # get the command from the user

        if command == 'left':
            player.j -= 1  # move left
        elif command == 'right':
            player.j += 1  # move right
        elif command == 'up':
            player.i -= 1  # move up
        elif command == 'down':
            player.i += 1  # move down

        entities = world.get_entities(player.i, player.j)
        entities.remove(player)
        if len(entities) > 0 and entities[0].icon == '§':
            print('You have encountered an enemy! 😮')





main()








