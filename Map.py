
from Block import Block
from Point import Point
import constants as C

class Map:

    def __init__(self, cell, hole, matrix):
        self.cell = cell
        self.hole = hole
        self.matrix = matrix
        self.height = len(matrix)
        self.width = len(matrix[0])

    def draw(self, screen):
        pnt = Point(0, 0)
        for i in self.matrix:
            for j in i:
                if j == 1:
                    screen.blit(self.cell, (pnt.x * C.CELL_SIZE, pnt.y * C.CELL_SIZE))
                elif j == 2:
                    screen.blit(self.hole, (pnt.x * C.CELL_SIZE, pnt.y * C.CELL_SIZE))
                pnt.x += 1
            pnt.x = 0    
            pnt.y += 1
    
    def inMap(self, point):
        return (0 <= point.x  and point.x < self.width) and (0 <= point.y and point.y < self.height) 

    def impact(self, block):
        if not self.inMap(block.fst_point) or not self.inMap(block.snd_point):
            print("Your Block Got Out The Map !!!")
            return 0

        fst_block_fell = self.matrix[block.fst_point.y][block.fst_point.x] == 0
        snd_block_fell = self.matrix[block.snd_point.y][block.snd_point.x] == 0
        if fst_block_fell or snd_block_fell:
            print("Your Block Fell !!!")
            return 0
        
        won_the_game = self.matrix[block.fst_point.y][block.fst_point.x] == 2 and \
                        block.status == Block.STANDING
        if won_the_game:
            print("You Won <--(^_^)-->")
            return 2

        return 1
