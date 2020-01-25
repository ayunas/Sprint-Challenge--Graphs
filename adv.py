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
start_room = traversal.graph[4]
end_room = traversal.graph[14]

# traverse.dft(player)
g = traversal.explore(player)
# print(g)

# dfs = traversal.dfs(4,14)
# print(dfs)

# dft = traversal.dft(4)

follow_dft = traversal.follow_dft(player,world,4)
print('follow_dft', follow_dft)
print('steps to explore room: ', len(follow_dft))

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


# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# print('room_graph', len(room_graph))

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
