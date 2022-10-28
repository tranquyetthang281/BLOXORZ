import time
import pygame
from Block import Block
from Map import Map
import constants as C
import copy
from State import *
from dfs import DepthFirstSearch

# init
pygame.init()

# set title
pygame.display.set_caption("Thang love Trang")
icon = pygame.image.load("imgs/icon.png")
pygame.display.set_icon(icon)

# state of the game
state = state1

# setting map
cell_map = pygame.image.load("imgs/map.png")
hole_map = pygame.image.load("imgs/hole.png")
matrix = state.matrix
map = Map(cell_map, hole_map, matrix)

# setting block
init_status = state.init_status
init_fst_point = state.init_fst_point
init_snd_point = state.init_snd_point
block_standing = pygame.image.load("imgs/block_standing.png")
block_lying = pygame.image.load("imgs/block_lying.png")
block = Block(init_status, block_standing, block_lying, copy.copy(init_fst_point), copy.copy(init_snd_point))

# create the screen
screen = pygame.display.set_mode((map.width * C.CELL_SIZE, map.height * C.CELL_SIZE))

# start game
dfs = DepthFirstSearch(map)
success, solution = dfs.solve(block)
i = 0
running = True
while running:
    screen.fill((255, 255, 255))
    if i < len(solution):
        block = solution[i]
        i += 1
    map.draw(screen)
    block.draw(screen)
    time.sleep(0.5)
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

#     # if map.impact(block) == True:
#     #     block.status = init_status
#     #     block.fst_point = copy.copy(init_fst_point)
#     #     block.snd_point = copy.copy(init_snd_point)

    pygame.display.update()
