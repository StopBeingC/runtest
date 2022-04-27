import random
import math
from numpy import true_divide
import pygame
import time

from sqlalchemy import null, true

pygame.init()

game_screen = pygame.display.set_mode((1440, 720))

icon = pygame.image.load('Runner_stickman.png')

pygame.display.set_caption("Stickman Game")

pygame.display.set_icon(icon)

# Player Image Animation
still = True
playeridleframe1 = pygame.image.load('idlef1.png')
playeridleframe2 = pygame.image.load('idlef2.png')
playerrunframe1 = pygame.image.load('runf1.png')
playerrunframe2 = pygame.image.load('runf2.png')

# Player
playerX = 720
playerY = 360
playerX_change = 0
playerY_change = 0

#Run class
class animation:
    
    def __init__(self, run1, run2, idle1, idle2):
        
        self.run1 = run1
        self.run2 = run2
        self.idle1 = idle1
        self.idle2 = idle2
    
    def run(self):
        
        global playerX # add x position
        global playerY # add y position
        global playerX_change
        global playerY_change
        global still # variable that will identify if animation is idle.
        
        if still: # if still
            
            playerX += playerX_change
            playerY += playerY_change
            
            game_screen.blit(self.idle1, (playerX, playerY)) # add x and y position
            pygame.display.update()
            time.sleep(1.5)
            game_screen.blit(self.idle2, (playerX, playerY)) # do same
            pygame.display.update()
            time.sleep(1.5)
                    
        elif still == False: # if not still (running)
            
           playerX += playerX_change
           playerY += playerY_change 
            
           game_screen.blit(self.run1, (playerX, playerY))
           pygame.display.update()
           time.sleep(1.5)
           game_screen.blit(self.run2, (playerX, playerY))
           pygame.display.update()
           time.sleep(1.5)

player1 = animation(playeridleframe1, playeridleframe2, playerrunframe1, playerrunframe2)

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
                
                playerX_change = 50
            
            elif events.type == pygame.K_LEFT:
                
                still = False
                
                playerX_change = -50
        
        elif events.type == pygame.KEYUP:
            
            if events.type == pygame.K_RIGHT or pygame.K_LEFT:
                
                still = True
                
                playerX_change = 0
    
    #Barriers
    
    if playerX >= 1440:
        playerX = 1440
    
    elif playerX <= 0:
        playerX = 0
    
    player1.run()
    
    pygame.display.update()