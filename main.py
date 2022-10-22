import time
import pygame
import constants as C
from Map import Map
from Block import Block
from Point import Point
# init
pygame.init()

# create the screen


# set title
pygame.display.set_caption("Thang love Trang")
icon = pygame.image.load("imgs/icon.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("imgs/spider.png")

playerX_change = 0
playerY_change = 0

# SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))



# start game
bs = C.BLOCK_SIZE
map = Map(C.map)
screen = pygame.display.set_mode((map.getHeight()*bs, map.getWidth()*bs))
map.draw(screen)
X = map.getInitial().x*bs
Y = map.getInitial().y*bs
running = True
block = Block( playerImg,Point(X, Y),)

while running:   
    screen.fill(C.GREEN)
    map.draw(screen)   
    block.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                block.move_left()
            if event.key == pygame.K_RIGHT:
                block.move_right()
            if event.key == pygame.K_UP:
                block.move_up() 
            if event.key == pygame.K_DOWN:
                block.move_down()

    pygame.display.update()
    
