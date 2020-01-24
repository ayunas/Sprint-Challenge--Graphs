from stack import Stack
import random


class Traversal:
    def __init__(self):
        self.graph = {}
        self.stack = Stack()
    
    def log_room(self,id,waze=None):
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
        

    def traverse(self,player):
        room = player.current_room
        print('starting room', room.id)
        room.get_exits()
        waze = self.graph[room.id]
        room_exits = list(waze.items())
        
        # while '?' in room_exits:  #while self.graph[room.id] has an unexplored exit
        # print(list(self.graph[room.id].items()))
        while '?' in list(self.graph[room.id].values()):
            exits = list(self.graph[room.id].items())
            print('room.id', room.id, 'exits', exits)
            way,i = random.choice(exits)
            print('random way',way)
            move = player.travel(way)
            print('moved to room_id:', move)

            if move == None:
                x = self.update_rooms(way[0],room)
                print('update move was none', x)
                
            else: #moved to the new room
                new_room = player.current_room
                y = self.update_rooms(way[0],room, new_room)
                print(f'update move was {way}', y)
                room = new_room
        return self.graph

    def dft(self,player):
        old_room = player.current_room
        old_exits = old_room.get_exits()

        for e in old_exits:
            player.travel(e)
            new_room = player.current_room
            new_exits = new_room.get_exits()
            flip = self.flip_way(e)
            self.log_room(new_room.id,(flip,old_room.id))
            self.log_room(old_room.id,(e,new_room.id))
        
        waze = self.graph[new_room.id]
        valid_waze = [room_id for room_id in list(waze.values()) if room_id != '?']
        print(valid_waze)
        print(self.graph)
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