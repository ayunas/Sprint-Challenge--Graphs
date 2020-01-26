class Queue:
    def __init__(self):
        self.data = []
    
    def enque(self,val):
        self.data.append(val)
        return self.data[-1]
    
    def deque(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        return None
    
    @property
    def size(self):
        return len(self.data)
    
    def __repr__(self):
        return str(self.data)


# q = Queue()
# q.enque([5])
# q.enque([5,10])
# q.enque([5,10,15])
# removed = q.deque()
# print(removed)
# print(q)

