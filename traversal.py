from stack import Stack
from world import World
import random
from ast import literal_eval


class Traversal:
    def __init__(self):
        self.graph = {}
        self.path = []
        # self.world = World()
        # map_file = "maps/test_loop_fork.txt"
        # f = open(map_file,'r').read()
        # room_graph = literal_eval(f)
        # self.world.load_graph(room_graph)
    
    def load_room(self,id,waze=None):
        # directions=['?','?','?','?']
        compass = {'n':'?','s':'?','e':'?','w':'?'}
        if waze:
            way,way_id = waze     
            compass[way] = way_id
            self.graph[id] = compass
        else:
            self.graph[id] = compass
    
    def dfs(self,start,end):
        pass

    def flip_way(self,جهة): #جهة pronounced "Jiha" is arabic meaning "direction"
        if جهة == 'n':
            عكس = 's' #عكس pronounced "'Aks" is arabic meaning "opposite"
        if جهة == 's':
            عكس = 'n'
        if جهة == 'e':
            عكس = 'w'
        if جهة == 'w':
            عكس = 'e'
        return عكس
    

    def update_rooms(self,way,old_room,new_room=None):
        if new_room == None:
            # self.log_room(old_room.id, (way,None))
            self.graph[old_room.id][way] = None
            return self.graph[old_room.id]
        else: #new_room has been passed in
            # self.log_room(old_room.id, (way,new_room.id))
            self.graph[old_room.id][way] = new_room.id
            flip = self.flip_way(way)
            # self.log_room(new_room.id, (flip,old_room.id))
            self.graph[new_room.id][flip] = old_room.id
            return (self.graph[old_room.id],self.graph[new_room.id])
        

    def explore(self,player):
        room = player.current_room
        explored = set()
       
        while len(explored) < len(list(self.graph)):
          
            exits = list(self.graph[room.id].items())
            way,i = random.choice(exits)
            move = player.travel(way)

            if move == None:
                x = self.update_rooms(way[0],room)
            else: #moved to the new room
                self.path.append(way)
                new_room = player.current_room
                y = self.update_rooms(way[0],room, new_room)
                exit_rooms = list(self.graph[new_room.id].values())
                if '?' not in exit_rooms:
                    explored.add(new_room)
                room = new_room
        return self.graph
    
    def duplicates(self,lst,item):
        return [i for i,x in enumerate(lst) if x == item]
    
    def follow_dft(self,player,world,start_id):
        #get the dft path.
        #move the player along each step of the dft path
        #if the player cannot move to the path step, find the dft link between the current room of the player and the next dft step path.  have the player tread the link provided.
        #then after treading the link, continue along the path from where player left off.

        world.print_rooms()
        player.current_room = world.rooms[start_id]
        path = self.dft(start_id)
        tread = [player.current_room.id]
        for i,step in enumerate(path):

            try:
                next_step = path[i+1]
            except IndexError:
                next_step = -1
            
            waze = self.graph[step]
            # next_way = {way : waze[way] for way in waze if waze[way] == next_step}
            next_way = [way for (way,room_id) in waze.items() if room_id == next_step]
            # print('next_way on the path', next_way)

            try:
                next_way = next_way[0]
            except IndexError: #the player doesnt have access to the next room
                next_way = -1

            if next_way != -1:
                player.travel(next_way)
                tread.append(player.current_room.id)
                # print('tread', tread)
            else:
                # print('player cannot access the next path step: ')
                # print('current_room', player.current_room.id)
                # print('next_step', next_step)
                # print('path', path)
                #self.bfs() will find shortest path
                link = self.dfs(player.current_room.id,next_step)
                # link.pop(0) #don't travel to same room, already in the room.
                # print('link', link)
                
                if link == None:
                    return tread

                for i,l in enumerate(link):
                    waze = self.graph[l]

                    try:
                        next_link = link[i+1]
                    except IndexError:
                        next_link = -1

                    next_step = [way for (way,next_id) in waze.items() if next_id == next_link]

                    try:
                        next_step = next_step[0]
                    except IndexError:
                        next_step = -1

                    if next_step != -1:
                        player.travel(next_step)
                        tread.append(player.current_room.id)
                        # print('tread', tread)

        
        

        # tread = list(path)
        # print('path', path)

        # for i,room_id in enumerate(path):
        #     # print('current room', player.current_room)
        #     print('path at beginning of for loop',path)
        #     try:
        #         next_path_id = path[i+1]
        #         # next_path_id = path.index(room_id)
        #         print('next_path_id', next_path_id)
        #         # dups = self.duplicates(path,room_id)
        #         # print('dups', dups)
        #         # next_path_id = dups[-1]+1
        #     except IndexError:
        #         next_path_id = -1

        #     next_rooms = list(self.graph[room_id].values())

        #     if next_path_id in next_rooms:
        #         player.current_room = world.rooms[next_path_id]
        # ##############################Sound Logic Till this point#######################################
        #     else: #next_path_id not in next_rooms
        #         print('player current room, next_id', room_id, next_path_id)
        #         link = self.dfs(room_id, next_path_id)
        #         link = link[1:]
        #         print('link', link)
        #         treadlinked = tread[:i+1] + link + tread[i+2:]
        #         # path = list(treadlinked)
        #         tread = treadlinked
        #         print('updated tread', tread)
        '''
        ***this code is valid for restepping 1 node only. but for multiple nodes, it wont work***
            print(self.graph[room_id])
            waze = self.graph[room_id]
            valid_waze = {way: waze[way] for way in waze.keys() if waze[way] is not None}
            print('valid waze', valid_waze)
            for way in valid_waze:
                next_room_id = waze[way]
                print('next room id', next_room_id)
                next_next_rooms = self.graph[next_room_id]
                print('next next rooms', next_next_rooms)
                print(next_path_id in next_next_rooms.values())
                if next_path_id in next_next_rooms.values():
                    tread = list(tread)
                    tread.insert(i+1,next_room_id)
                    print('tread path after insert', tread)
            #         player.current_room = self.graph[next_room_id]
        '''

            #if the next room_id in path is in the self.graph[room_id]
            #grab the way and player.travel(way)
            # print(self.graph[room_id])
            # player.travel()
            # print(path[i+1])
            #if the next_id in path is not in the self.graph[room_id],
                #get the next rooms for all the next_rooms of the current room.  if any of those contain
                #the next_id in path, travel to that room
        print('tread', tread)
    
    def dft(self,start_id):
        stack = Stack()
        next_rooms = self.graph[start_id]
        for way in next_rooms:
            if next_rooms[way] != None:
                stack.push(next_rooms[way])
        
        visited = [start_id]

        while stack.size > 0:
            room_id = stack.pop()
            if room_id not in visited:
                visited.append(room_id)
                next_rooms = self.graph[room_id]
                for way in next_rooms:
                    if next_rooms[way] != None:
                        stack.push(next_rooms[way])
        return visited

    
    def dfs(self,start_room_id,end_room_id):
        stack = Stack()

        initial_path = [start_room_id]
        stack.push(initial_path)
        
        visited = set()

        while stack.size > 0:
            path = stack.pop()
            room_id = path[-1] #get latest room in the latest path
            
            if room_id not in visited:
                if room_id == end_room_id:
                    return path
                else:
                    visited.add(room_id)
                
                next_rooms = self.graph[room_id]

                for way in next_rooms:
                    if next_rooms[way] == None:
                        continue
                    else:
                        new_path = list(path)
                        new_path.append(next_rooms[way])
                        stack.push(new_path)
            
    def __repr__(self):
        return str(self.graph)