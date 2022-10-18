
import constants as C

class Block:

    # status of block
    LYING_HORIZONTALLY = 1
    LYING_VERTICALLY = 2
    STANDING = 3

    def __init__(self, status, standing, lying, fst_point, snd_point):
        self.status = status
        self.standing = standing
        self.lying = lying
        self.fst_point = fst_point
        self.snd_point = snd_point

    def draw(self, screen):
        if(self.status == Block.STANDING):
            screen.blit(self.standing, (self.fst_point.x * C.CELL_SIZE, self.fst_point.y * C.CELL_SIZE))
        else:
            screen.blit(self.lying, (self.fst_point.x * C.CELL_SIZE, self.fst_point.y * C.CELL_SIZE))
            screen.blit(self.lying, (self.snd_point.x * C.CELL_SIZE, self.snd_point.y * C.CELL_SIZE))

    def move_up(self):
        if self.status == Block.STANDING:
            self.status = Block.LYING_VERTICALLY
            self.fst_point.y -= 1
            self.snd_point.y -= 2
        elif self.status == Block.LYING_VERTICALLY:
            self.status = Block.STANDING
            self.fst_point.y -= 2
            self.snd_point.y -= 1
        elif self.status == Block.LYING_HORIZONTALLY:
            self.fst_point.y -= 1
            self.snd_point.y -= 1

    def move_down(self):
        if self.status == Block.STANDING:
            self.status = Block.LYING_VERTICALLY
            self.fst_point.y += 2
            self.snd_point.y += 1
        elif self.status == Block.LYING_VERTICALLY:
            self.status = Block.STANDING
            self.fst_point.y += 1
            self.snd_point.y += 2
        elif self.status == Block.LYING_HORIZONTALLY:
            self.fst_point.y += 1
            self.snd_point.y += 1

    def move_right(self):
        if self.status == Block.STANDING:
            self.status = Block.LYING_HORIZONTALLY
            self.fst_point.x += 1
            self.snd_point.x += 2
        elif self.status == Block.LYING_VERTICALLY:
            self.fst_point.x += 1
            self.snd_point.x += 1
        elif self.status == Block.LYING_HORIZONTALLY:
            self.status = Block.STANDING
            self.fst_point.x += 2
            self.snd_point.x += 1

    def move_left(self):
        if self.status == Block.STANDING:
            self.status = Block.LYING_HORIZONTALLY
            self.fst_point.x -= 2
            self.snd_point.x -= 1
        elif self.status == Block.LYING_VERTICALLY:
            self.fst_point.x -= 1
            self.snd_point.x -= 1
        elif self.status == Block.LYING_HORIZONTALLY:
            self.status = Block.STANDING
            self.fst_point.x -= 1
            self.snd_point.x -= 2
