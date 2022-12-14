import pygame
import time
import random
import numpy as np
import grid

width, height = 1200,720
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

#scaler = 30
scaler = 20
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_z:
                Grid.restart()

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)
    pygame.display.update()

pygame.quit()
