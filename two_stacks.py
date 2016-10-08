class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        return self.first[0]
        
    def pop(self):
        self.second.pop()
        self.first=[]
        for i in xrange(0, len(self.second)):
            self.first.append(self.second[len(self.second) - i - 1])
        
        
    def put(self, value):
        self.first.append(value)
        self.second = []
        for i in xrange(0, len(self.first)):
            self.second.append(self.first[len(self.first) - i - 1])

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
