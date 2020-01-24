from room import Room
from player import Player
from world import World
from traversal import Traversal

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)



# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']




'''
get id of current room.
create a new traversal entry of current room.

go out an exit. store the direction travelled
create a new entry for the new room id, the opposite direction is the prev_room_id.
update the previous room id entry.  the exit taken == id of current room
player.travel(exits[0])
player.current_room.id
'''

traverse = Traversal()
start_room = player.current_room
traverse.add_room(start_room.id)
exits = start_room.get_exits()
جهة = random.choice(exits)  #in Arabic:  جهة pronounced "Jiha" means direction
player.travel(جهة)
next_room_id = player.current_room.id

if جهة == 'n':
    back_exit = 's'
if جهة == 's':
    back_exit = 'n'
if جهة == 'e':
    back_exit = 'w'
if جهة == 'w':
    back_exit = 'e'

print('traverse', traverse)
back_exit = (back_exit,start_room.id)
traverse.add_room(player.current_room.id, back_exit)
print('traverse', traverse)
way = (جهة,player.current_room.id)
traverse.add_room(start_room.id,way)
print('traverse', traverse)

# traversal.add_room(room.id)




# if 'n' not in exits:
#     exits.insert(0,'?')
# if 's' not in exits:
#     exits.insert(1,'?')
# if 'e' not in exits:
#     exits.insert(2,'?')
# if 'w' not in exits:
#     exits.insert(3,'?')



traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)



# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
