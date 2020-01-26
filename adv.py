from room import Room
from player import Player
from world import World
from traversal import Traversal

import random
from ast import literal_eval


# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)
print('initial player starting room', player.current_room.id, 'world.start room', world.starting_room.id)

traversal = Traversal()
start_room = player.current_room

def load_rooms(world):
    for r in world.rooms:
        # print(room)
        r_id = world.rooms[r].id
        traversal.load_room(r_id)

load_rooms(world)

random_traversal = traversal.explore(player)
print('# of moves to randomly explore entire map: ', len(random_traversal))


player.current_room = world.starting_room
print('player starting room before follow_dft', player.current_room.id)
follow_dft = traversal.follow_dft(player,world)

################################TRAVERSAL TEST#########################################
player.current_room = world.starting_room
traversal_path = follow_dft
visited_rooms = set()
visited_rooms.add(player.current_room)

print('room_graph length: ', len(room_graph))
print('player starting room: ', player.current_room.id)
print('follow_dft', follow_dft)

for i,room_id in enumerate(traversal_path):
    try:
        next_step = traversal_path[i+1]
    except IndexError:
        next_step = -1

    if room_id != '?':
        waze = traversal.graph[room_id]
        way = [way for (way,next_room_id) in waze.items() if next_room_id == next_step]

    try:
        way = way[0]
    except: #there was no way found matching the next_room_id in the traversal path. probably reached the end of the list
        break

    player.travel(way)
    visited_rooms.add(player.current_room)

visits = set()
for v in visited_rooms:
    visits.add(v.id)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
