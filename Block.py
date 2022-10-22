import pygame
import constants as C
from Point import Point
cat = pygame.image.load("imgs/cat2.png")
spider = pygame.image.load("imgs/spider.png")
class Block:
    def __init__(self, img, p1,stand= True):        
        self.img = img
        self.p1 = p1
        self.p2 = None
        self.stand= stand

    def move_up(self):
        if self.stand:
            print("stand")
            self.toLie()
            self.p1.set(self.p1.x, self.p1.y-C.ONE_MOVE)
            self.p2.set(self.p1.x, self.p1.y-C.ONE_MOVE)
        else:
            if self.p1.y == self.p2.y:
                print("keep lying")
                self.p1.set(self.p1.x, self.p1.y - C.ONE_MOVE)
                self.p2.set(self.p2.x, self.p2.y- C.ONE_MOVE)
            else:
                print("lying to stand")
                self.p1.set(self.p1.x, min(self.p1.y,self.p2.y) - C.ONE_MOVE)
                self.toStand()

    def move_down(self):
        if self.stand:
            self.toLie() 
            self.p1.set(self.p1.x, self.p1.y+C.ONE_MOVE)
            self.p2.set(self.p1.x, self.p1.y+C.ONE_MOVE)
        else:
            if self.p1.y == self.p2.y:
                print("keep lying")
                self.p1.set(self.p1.x, self.p1.y + C.ONE_MOVE)
                self.p2.set(self.p2.x, self.p2.y+ C.ONE_MOVE)
            else:
                print("down:lying to stand")
                self.p1.set(self.p1.x, max(self.p1.y,self.p2.y) + C.ONE_MOVE)
                self.toStand()

    def move_left(self):
        if self.stand:
            self.toLie()
            self.p1.set(self.p1.x-C.ONE_MOVE, self.p1.y)
            self.p2.set(self.p1.x-C.ONE_MOVE, self.p1.y)   
        else:
            if self.p1.y == self.p2.y:
                print("left:lying to stand")  
                self.p1.set(min(self.p1.x,self.p2.x) -C.ONE_MOVE, self.p1.y )                 
                self.toStand()         
            else:
                print("keep lying")      
                self.p1.set(self.p1.x -C.ONE_MOVE, self.p1.y )
                self.p2.set(self.p2.x-C.ONE_MOVE, self.p2.y)  

    def move_right(self):
        if self.stand:
            self.toLie()
            self.p1.set(self.p1.x+C.ONE_MOVE, self.p1.y)
            self.p2.set(self.p1.x+C.ONE_MOVE, self.p1.y)   
        else:
            if self.p1.y == self.p2.y:
                print("right:lying to stand")             
                self.p1.set(max(self.p1.x,self.p2.x) +C.ONE_MOVE, self.p1.y )
                self.toStand()                  
            else:
                print("keep lying")      
                self.p1.set(self.p1.x +C.ONE_MOVE, self.p1.y )
                self.p2.set(self.p2.x+C.ONE_MOVE, self.p2.y)   

    def draw(self, screen):
        screen.blit(self.img, (self.p1.x, self.p1.y))
        if self.p2:
            screen.blit(self.img, (self.p2.x, self.p2.y))  

    def toLie(self):
        self.stand = False
        self.img = cat 
        if self.p2 is None:
            self.p2 = Point()

    def toStand(self):
        self.stand = True 
        self.img = spider  
        self.p2 = None
            
