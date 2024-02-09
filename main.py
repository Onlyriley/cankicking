import pygame
import os
from random import randint
import threading
from time import sleep

CANSIZE = 100
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Can kickin")
pygame.font.init()
FPS = 60

GENERAL_FONT = pygame.font.SysFont("comicsans", 30)

GRAVITY = 20

class Can:
    def __init__(self):
        # posX/Y determine the center of the object
        self.posX = 0
        self.posY = 0
        self.clicks = 0
        self.stage = 0
        self.veloX = 0
        self.veloY = 0

class Assets:
    def __init__(self):
        self.canSprites = []
    def populateSprites(self):
        self.canSprites.append(pygame.image.load(os.path.join('sprites', 'can.png')).convert_alpha())
        self.canSprites.append(pygame.image.load(os.path.join('sprites', 'can2.png')).convert_alpha())
        self.canSprites.append(pygame.image.load(os.path.join('sprites', 'can3.png')).convert_alpha())
        
class GameState:
    def __init__(self):
        self.score = 0
        self.run = True
        self.objects = []
        self.spawnrate = 20
        
assets = Assets()
assets.populateSprites()

game = GameState()

############################

def draw_window():
    for can in game.objects:
        WIN.blit(assets.canSprites[can.stage], (can.posX, can.posY))
    
    pygame.display.update()

def getClickedObject():
    clicked = []
    mouse = pygame.mouse.get_pos() # x = [0], y = [1]
    for can in game.objects:
        if can.posX - CANSIZE <= mouse[0] <= can.posX + CANSIZE:
            pass # need Y values still

def spawnCan():
    game.objects.append(Can())
    
def main():
    
    spawnTick = 0
    clock = pygame.time.Clock()
    
    while game.run:
        clock.tick()
        spawnTick += 1
        
        if spawnTick >= FPS * game.spawnrate:
            spawnCan()
            spawnTick = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickedObject = getClickedObject()

    draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()