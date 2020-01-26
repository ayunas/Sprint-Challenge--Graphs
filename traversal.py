from stack import Stack
from queue import Queue
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
        # print('player starting room in explore', player.current_room.id)
        room = player.current_room
        explored = set()
        path = []
       
        while len(explored) < len(list(self.graph)):
          
            exits = list(self.graph[room.id].items())
            way,next_id = random.choice(exits)
            move = player.travel(way)

            if move == None:
                x = self.update_rooms(way[0],room)
            else: #moved to the new room
                path.append(next_id)
                new_room = player.current_room
                y = self.update_rooms(way[0],room, new_room)
                exit_rooms = list(self.graph[new_room.id].values())
                if '?' not in exit_rooms:
                    explored.add(new_room)
                room = new_room
        # path = [step for step in path if step != '?']
        return path
    
    def duplicates(self,lst,item):
        return [i for i,x in enumerate(lst) if x == item]
    
    def follow_dft(self,player,world):
        #get the dft path.
        #move the player along each step of the dft path
        #if the player cannot move to the path step, find the dft link between the current room of the player and the next dft step path.  have the player tread the link provided.
        #then after treading the link, continue along the path from where player left off.
        # world.print_rooms()

        start_id = player.current_room.id
        # print('starting room in follow_dft', start_id)
        # player.current_room = world.rooms[start_id]
        path = self.dft(start_id)
        # path = self.bft(start_id)
        # print('bft path', path)
        tread = [player.current_room.id]
        for i,step in enumerate(path):
            try:
                next_step = path[i+1]
            except IndexError:
                next_step = -1
            
            waze = self.graph[step]
            # next_way = {way : waze[way] for way in waze if waze[way] == next_step}
            next_way = [way for (way,room_id) in waze.items() if room_id == next_step]
            # print('room', step)
            # print('exits',waze)


            try:
                next_way = next_way[0]
            except IndexError: #the player doesnt have access to the next room
                next_way = -1
                # next_way = step #path[i]
                # print('no next way in path', next_way)

            if next_way != -1:
                player.travel(next_way)
                tread.append(player.current_room.id)
                # print('tread', tread)
            else:
                # print('player cannot access the next room in path.  need a link')
                # print('current room', player.current_room.id)
                # print('next room in path', next_step)

                ####'''Depth First Search & Breadth First Search both work for backtracking. ####
                #### Choose either to see differences in moves'''####

                # link = self.dfs(player.current_room.id,next_step)
                link = self.bfs(player.current_room.id,next_step)
                # print('link', link)
                
                # if link == None:
                #     return tread

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
                        # print('next room', player.current_room.id)
                        tread.append(player.current_room.id)
                        # print('tread', tread)
        return tread

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

    def bft(self,start_room_id):
        queue = Queue()
        waze = self.graph[start_room_id]
        for way in waze:
            if waze[way] != None:
                queue.enque(waze[way])
        
        visited = [start_room_id]

        while queue.size > 0:
            room_id = queue.deque()
            if room_id not in visited:
                visited.append(room_id)
                waze = self.graph[room_id]
                for way in waze:
                    if waze[way] != None:
                        queue.enque(waze[way])
        return visited


    def dfs(self,start_room_id,end_room_id):
        stack = Stack()

        # print('end_room_id in dfs', end_room_id)
        initial_path = [start_room_id]
        stack.push(initial_path)

        if end_room_id == -1:
            return initial_path
        
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
            # print('stack', stack)


    def bfs(self,start_room_id,end_room_id):
        # print('end_room_id in bfs', end_room_id)

        queue = Queue()
        
        initial_path = [start_room_id]
        queue.enque(initial_path)

        if end_room_id == -1:
            return initial_path

        visited = set()

        while queue.size > 0:
            path = queue.deque()
            room_id = path[-1]

            if room_id not in visited:
                if room_id == end_room_id:
                    return path
                else:
                    visited.add(room_id)
            
            waze = self.graph[room_id]

            for way in waze:
                if waze[way] == None:
                    continue
                else:
                    new_path = list(path)
                    new_path.append(waze[way])
                    queue.enque(new_path)
            # print('queue', queue)

    def __repr__(self):
        return str(self.graph)