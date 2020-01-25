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
        # print('starting room', room.id)
        # room.get_exits()
        # waze = self.graph[room.id]
        # exit_rooms = list(waze.values())
        # exit_ways = list(waze)
        
        explored = set()
        # while '?' in room_exits:  #while self.graph[room.id] has an unexplored exit
        # print(list(self.graph[room.id].items()))
        
        # while '?' in list(self.graph[room.id].values()):
        # while '?' in exit_rooms:
        while len(explored) < len(list(self.graph)):
            # print('explored', len(explored))
            # print('self.graph', len(list(self.graph.items())))

            exits = list(self.graph[room.id].items())
            # print('room.id', room.id, 'exits', exits)
            way,i = random.choice(exits)
            # print('random way',way)
            move = player.travel(way)
            # print('moved to room_id:', move)

            if move == None:
                x = self.update_rooms(way[0],room)
                # print('update move was none', x)
                
            else: #moved to the new room
                self.path.append(way)
                new_room = player.current_room
                y = self.update_rooms(way[0],room, new_room)
                exit_rooms = list(self.graph[new_room.id].values())
                # print('exit_rooms',exit_rooms)
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

    
    def longest_dfs(self,start_room_id,end_room_id):
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
                    # print(way,next_rooms[way])
                    if next_rooms[way] == None:
                        continue
                    else:
                        new_path = list(path)
                        new_path.append(next_rooms[way])
                        stack.push(new_path)
        
        # return self.stack

        # waze = list(room.items())

        # valid_waze = [(w,id) for w,id in waze if id]
        # way,next_room_id = random.choice(valid_waze)

        # if next_room_id not in visited:
        #     if next_room_id == end_room_id:
        #         return path
        #     visited.add(next_room_id)

        #     next_waze = self.graph[next_room_id]

        #     for way in next_waze:
        #         if next_waze[way] != None:
        #             fresh_path = list(path)
        #             fresh_path.append(next_waze[way])
        #             self.stack.push(fresh_path)
        
                



    # def dft(self,player):
    #     old_room = player.current_room
    #     old_exits = old_room.get_exits()

    #     for e in old_exits:
    #         player.travel(e)
    #         new_room = player.current_room
    #         new_exits = new_room.get_exits()
    #         flip = self.flip_way(e)
    #         self.log_room(new_room.id,(flip,old_room.id))
    #         self.log_room(old_room.id,(e,new_room.id))
        
    #     waze = self.graph[new_room.id]
    #     valid_waze = [room_id for room_id in list(waze.values()) if room_id != '?']
    #     print(valid_waze)
    #     print(self.graph)
        # while len(valid_waze):
        #     pass
    


        # waze = self.graph[start_room.id]
        # valid_waze = [(w,i) for w,i in list(waze.items()) if i != '?']
       
        # if len(valid_waze) > 0:
        #     valid_waze = dict(valid_waze)
        #     for way in valid_waze:
        #         player.travel(way)
        #         new_room = player.current_room
        #         self.stack.push(new_room)
        #     # w_id = player.current_room.id

        # visited = {start_room}
        
        # while self.stack.size > 0:
        #     next_room = self.stack.pop()
        #     print('next_room', next_room)
        #     if next_room not in visited:
        #         visited.add(next_room)
        #         waze = self.graph[next_room.id]
        #         for w in waze:
        #             print('way', w)
        #             player.travel(w)
        #             w_id = player.current_room.id
        #             print('w_id', w_id)
        #             self.stack.push(w_id)
        
        # return visited
                # next_way = random.choice(list(exits))
                # print('next way', next_way)

            
    def __repr__(self):
        return str(self.graph)