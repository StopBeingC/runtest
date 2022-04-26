import random
import math
import pygame
import time

pygame.init()

class run:
    
    def __init__(self, runframe1, runframe2, idle1, idle2):
        
        self.runframe1 = runframe1
        self.runframe2 = runframe2
        self.idle1 = idle1
        self.idle2 = idle2
        
    
        
pygame.image.load('idlef1.png')
pygame.image.load('idlef2.png')
pygame.image.load('runf1.png')
pygame.image.load('runf2.png')
