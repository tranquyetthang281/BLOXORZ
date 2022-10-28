
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

    def move_up(self, map):
        log_block = self.deepcopy()
        r = self.deepcopy()
        if r.status == Block.STANDING:
            r.status = Block.LYING_VERTICALLY
            r.fst_point.y -= 1
            r.snd_point.y -= 2
        elif r.status == Block.LYING_VERTICALLY:
            r.status = Block.STANDING
            r.fst_point.y -= 2
            r.snd_point.y -= 1
        elif r.status == Block.LYING_HORIZONTALLY:
            r.fst_point.y -= 1
            r.snd_point.y -= 1
        if map.impact(r) == 0:
            r.shallowcopy(log_block)
        return r

    def move_down(self, map):
        log_block = self.deepcopy()
        r = self.deepcopy()
        # print("ilu1:",self)
        if r.status == 3:
            r.status = 2
            r.fst_point.y += 2
            r.snd_point.y += 1
            # print("ilu:",self)
        elif r.status == Block.LYING_VERTICALLY:
            r.status = Block.STANDING
            r.fst_point.y += 1
            r.snd_point.y += 2
        elif r.status == Block.LYING_HORIZONTALLY:
            r.fst_point.y += 1
            r.snd_point.y += 1
        if map.impact(r) == 0:
            r.shallowcopy(log_block)
        return r


    def move_right(self, map):
        log_block = self.deepcopy()
        r = self.deepcopy()
        if r.status == Block.STANDING:
            r.status = Block.LYING_HORIZONTALLY
            r.fst_point.x += 1
            r.snd_point.x += 2
        elif r.status == Block.LYING_VERTICALLY:
            r.fst_point.x += 1
            r.snd_point.x += 1
        elif r.status == Block.LYING_HORIZONTALLY:
            r.status = Block.STANDING
            r.fst_point.x += 2
            r.snd_point.x += 1
        if map.impact(r) == 0:
            r.shallowcopy(log_block)
        return r

    def move_left(self, map):
        log_block = self.deepcopy()
        r = self.deepcopy()
        if r.status == Block.STANDING:
            r.status = Block.LYING_HORIZONTALLY
            r.fst_point.x -= 2
            r.snd_point.x -= 1
        elif r.status == Block.LYING_VERTICALLY:
            r.fst_point.x -= 1
            r.snd_point.x -= 1
        elif r.status == Block.LYING_HORIZONTALLY:
            r.status = Block.STANDING
            r.fst_point.x -= 1
            r.snd_point.x -= 2
        if map.impact(r) == 0:
            r.shallowcopy(log_block)
        return r
    def encode(self):
        return int(str(self))
    
    def __str__(self):
        return  str(self.status) + str(self.fst_point)

    # def __equal__(self, other):
    #     return self.status == other.status and self.fst_point == other.fst_point
    
    def deepcopy(self):
        return Block(self.status, self.standing, self.lying, self.fst_point.deepcopy(), self.snd_point.deepcopy())
    
    def shallowcopy(self, other):
        self.status = other.status 
        self.standing = other.standing
        self.lying = other.lying
        self.fst_point = other.fst_point
        self.snd_point = other.snd_point       