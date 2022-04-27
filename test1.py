import random
import math
from numpy import true_divide
import pygame
import time

from sqlalchemy import null, true

pygame.init()

game_screen = pygame.display.set_mode((1440, 720))

# Player Image Animation
still = null
playeridleframe1 = pygame.image.load('idlef1.png')
playeridleframe2 = pygame.image.load('idlef2.png')
playerrunframe1 = pygame.image.load('runf1.png')
playerrunframe2 = pygame.image.load('runf2.png')

#Run class
class animation:
    
    def __init__(self, run1, run2, idle1, idle2):
        
        self.run1 = run1
        self.run2 = run2
        self.idle1 = idle1
        self.idle2 = idle2
    
        def run():
            
            global playerX # add x position
            global playerY # add y position
            global still # variable that will identify if animation is idle.
            
            if still: # if still
                
                game_screen.blit(idle1, (playerX, playerY)) # add x and y position
                time.sleep(1.5)
                game_screen.blit(idle2, (playerX, playerY)) # do same
                time.sleep(1.5)
            
            if still == False: # if not still (running)
                
                game_screen.blit(run1, (playerX, playerY))
                time.sleep(1.5)
                game_screen.blit(run2, (playerX, playerY))
                time.sleep(1.5)

# Player
playerX = 720
playerY = 360
playerX_change = 0
playerY_change = 0

player = animation(playeridleframe1, playeridleframe2, playerrunframe1, playerrunframe2)

def playerf(playerX, playerY, playerX_change, playerY_change):
    
    playerX += playerX_change
    
    playerY += playerY_change
    
game_running = true

# Game Running

while game_running:
    
    game_screen.fill((255, 255, 255))
    
    #User Input
    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            
            game_running = False
        
        if events.type == pygame.KEYDOWN:
            
            if events.type == pygame.K_RIGHT:
                
                still = False
                
                playerX_change = 5
            
            if events.type == pygame.K_LEFT:
                
                still = False
                
                playerX_change = -5
        
        if events.type == pygame.KEYUP:
            
            if events.key == pygame.K_RIGHT or pygame.K_LEFT:
                
                still = True
                
                playerX_change = 0
    
    #Barriers
    
    if playerX >= 1440:
        playerX = 1440
    
    elif playerX <= 0:
        playerX = 0
    
    playerf(playerX, playerY, playerX_change, playerY_change)
    player.run()
    
    pygame.display.update()