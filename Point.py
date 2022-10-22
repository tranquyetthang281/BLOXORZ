class Point:
    def __init__(self, x = -1, y = -1):
        self.x = x 
        self.y = y
    def set(self, x, y):
        self.x = x
        self.y = y
    def add(self, x,y):
        self.x += x 
        self.y += y