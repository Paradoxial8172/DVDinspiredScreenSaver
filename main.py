import pygame
import math
import random
import tkinter
from tkinter import *
import os

# Variables
FPS = 60 #Int
pygame.init()
pygame.font.init()
screenWidth = 1000 #Int
screenHeight = 600 #Int
playerX = 0 #random.randint(0,936) #Int
playerY = 0 #random.randint(0,536) #Int
window = pygame.display.set_mode((screenWidth,screenHeight))
playerVelocityX = 5 #Int
playerVelocityY = 5 #Int
playerWidth = 64 #Int
playerHeight = 64 #Int
bgColor = 0,0,0 #RGB
R = random.randint(1,255)
G = random.randint(1,255)
B = random.randint(1,255)
playerColor = R,G,B
hits = 0
font = pygame.font.Font('freesansbold.ttf',25)
pygame.display.set_caption("game") #Str
 
def hitsCounter():
    global hits
    screenText = font.render(f'Hits: {hits}',True,(255,255,255))
    window.blit(screenText, (0,15))
    
def hitsValue():
    global hits
    hits = hits + 1  
               
def movement():
    global playerX, playerY, playerHeight, playerWidth, playerVelocityX, playerVelocityY   
    playerX = playerX + playerVelocityX
    playerY = playerY + playerVelocityY

#X coordiante plane:
    if playerX >= 936:
        colorChange()
        hitsValue()
        playerVelocityX = -5
        playerX = playerX + playerVelocityX
    if playerX <= 0:
        colorChange()
        hitsValue()
        playerVelocityX = 5
        playerX = playerX + playerVelocityX
#Y coordinate plane:
    if playerY >= 536:
        colorChange()
        hitsValue()
        playerVelocityY = -5
        playerY = playerY + playerVelocityY        
    if playerY <= 0:
        colorChange()
        hitsValue()
        playerVelocityY = 5
        playerY = playerY + playerVelocityY
        
def colorChange():
    global playerColor, playerX, playerY
    R = random.randint(1,255)
    G = random.randint(1,255)
    B = random.randint(1,255)
    playerColor = R,G,B

# Game loop
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False            
            
    window.fill((bgColor))
    pygame.draw.rect(window, playerColor, (playerX,playerY,playerWidth,playerHeight))

    hitsCounter()
    movement()
    pygame.display.update()
