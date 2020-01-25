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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal = Traversal()
start_room = player.current_room

def load_rooms(world):
    for r in world.rooms:
        # print(room)
        r_id = world.rooms[r].id
        traversal.load_room(r_id)

load_rooms(world)

# start_room = player.current_room
# start_room_id = traversal.graph[0]
# end_room = traversal.graph[14]

# traverse.dft(player)
g = traversal.explore(player)
# print(g)

# dfs = traversal.dfs(4,14)
# print(dfs)

# dft = traversal.dft(4)
# start_id = world.starting_room.id
start = world.rooms[4]
print('player starting room: ', start.id)
follow_dft = traversal.follow_dft(player,world,start.id)
# print('follow_dft', follow_dft)
# print('steps to explore map: ', len(follow_dft))

# traversal.add_room(room.id)

# if 'n' not in exits:
#     exits.insert(0,'?')
# if 's' not in exits:
#     exits.insert(1,'?')
# if 'e' not in exits:
#     exits.insert(2,'?')
# if 'w' not in exits:
#     exits.insert(3,'?')


# traversal_path = graph.path
traversal_path = follow_dft


# # TRAVERSAL TEST
visited_rooms = set()
# player.current_room = world.starting_room
player.current_room = start
visited_rooms.add(player.current_room)

print('room_graph length: ', len(room_graph))
print('player starting room: ', player.current_room.id)

for i,room_id in enumerate(traversal_path):
    # room = world.rooms[room_id]
    try:
        next_step = traversal_path[i+1]
    except IndexError:
        next_step = -1
    
    waze = traversal.graph[room_id]
    way = [way for (way,next_room_id) in waze.items() if next_room_id == next_step]

    try:
        way = way[0]
    except:
        break

    player.travel(way)
    visited_rooms.add(player.current_room)

visits = set()
for v in visited_rooms:
    visits.add(v.id)
print('visits', visits)
print('traversal_path', traversal_path)


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
