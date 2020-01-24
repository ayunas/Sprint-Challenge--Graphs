class Traversal:
    def __init__(self):
        self.graph = {}
    
    def add_room(self,id,exit=None):
        # directions=['?','?','?','?']
        compass = {'n':'?','s':'?','e':'?','w':'?'}

        if exit:
            way,way_id = exit        
            compass[way] = way_id
        else:
            self.graph[id] = compass
        
        # new_compass =  {key: id for key in compass if key == exit}
        # print('compass', new_compass)
        # n,s,e,w = directions
        # {'n': n, 's': s, 'e': e, 'w': w}

        self.graph[id] = compass
        pass
    
    def dfs(self,start,end):
        pass

    def dft(self,start):
        pass

    def __repr__(self):
        return str(self.graph)