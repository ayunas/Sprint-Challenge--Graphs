class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
        return self.stack[-1]
    
    def pop(self):
        if len(self.stack) >= 1:
            return self.stack.pop()
        else:
            return None
            
    @property
    def size(self):
        return len(self.stack)

    def __repr__(self):
        return str(self.stack)
