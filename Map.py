
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

    def impact(self, block):
        fst_block_out = block.fst_point.x >= self.width or block.fst_point.x < 0 or \
                        block.fst_point.y >= self.height or block.fst_point.y < 0
        snd_block_out = block.snd_point.x >= self.width or block.snd_point.x < 0 or \
                        block.snd_point.y >= self.height or block.snd_point.y < 0
        if fst_block_out or snd_block_out:
            print("Your Block Got Out The Map !!!")
            return True

        fst_block_fell = self.matrix[block.fst_point.y][block.fst_point.x] == 0
        snd_block_fell = self.matrix[block.snd_point.y][block.snd_point.x] == 0
        if fst_block_fell or snd_block_fell:
            print("Your Block Fell !!!")
            return True
        
        won_the_game = self.matrix[block.fst_point.y][block.fst_point.x] == 2 and \
                        block.status == Block.STANDING
        if won_the_game:
            print("You Won <--(^_^)-->")
            return True

        return False
