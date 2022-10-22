import constants as C
import pygame
from Point import Point
class Map:
    def __init__(self, map):
        self.map = map
        self.initial = Point()
    def draw(self, screen):
        bs = C.BLOCK_SIZE
        for i in range(len(self.map[0])):
            for j in range(len(self.map)):
                rect = pygame.Rect(i*bs, j*bs, bs,bs)
                color = C.GREEN
                if self.map[j][i] == 1:
                    color = C.ORANGE
                elif self.map[j][i] == 2:
                    color = C.WHITE
                elif self.map[j][i] == 3:
                    self.initial.set(i,j)
                    color = C.BLACK
                pygame.draw.rect(screen, color, rect, C.LINE_WIDTH)
    def getWidth(self):
        return len(self.map)

    def getHeight(self):
        return len(self.map[0])
    
    def getInitial(self):
        return self.initial
