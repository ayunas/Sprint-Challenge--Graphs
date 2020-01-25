from stack import Stack
import random


class Traversal:
    def __init__(self):
        self.graph = {}
        self.path = []
    
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