import pygame

# init
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# set title
pygame.display.set_caption("Thang love Trang")
icon = pygame.image.load("imgs/icon.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("imgs/spider.png")
playerX = 370
playerY = 420
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# start game
running = True
while running:
    screen.fill((128, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
