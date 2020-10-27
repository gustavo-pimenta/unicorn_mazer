#################################################################################
#   Name: Unicorn Mazer                                                         #
#   Version : 8.0                                                               #
#                                                                               #            
#   Made by:                                                                    #
#       Gustavo Pimenta_____Developer / Coder                                   #
#       Elayres Abreu_______Art director / Pixel Art Designer                   #
#                                                                               #          
#################################################################################    

import pygame
from pygame.locals import *
import pygame.mixer
import time
import random
from random import randrange
import sys
import csv

def num6dig(num): # always keep six numbers in the score 
    l = ['0','0','0','0','0','0']
    index = 6
    while (num !=0):
        l.insert(index, str(num%10))
        num = num // 10
        index -= 1
    
        l.pop(0)
    return ''.join(l)

def screen_print(sprite, size, pos):
    second_screen.blit(pygame.transform.scale(sprite, size), pos)

pygame.init() # start pygame system
width = 500 # initial width of the screen when the game opens
height = 800 # initial height of the screen when the game opens
screen = pygame.display.set_mode((height,width),RESIZABLE) # create the screen
second_screen = screen.copy() # create the second screen

start_menu = True
uni = pygame.image.load('game_files/images/uni.png')


while True: # game main loop
    
    while start_menu:

        for event in pygame.event.get():
        
            if event.type == QUIT: # when the player close the game
                pygame.display.quit()

            elif event.type == VIDEORESIZE: # when the player resize the window
                
                new_size = event.dict['size'] # get the new size
                new_size = list(new_size) # turns the tuple into a list
                new_size[1] = int(new_size[0]*0.625) # keep the window proporsions
                height, width = new_size # update vars with the new size value
                screen = pygame.display.set_mode((height,width),RESIZABLE) # recreate the screen with the new size
                print('SCREEN RESOLUTION = (', width, ',', height, ')') # print output 

        screen_print(uni, (100,100), (300,300))

        screen.blit(pygame.transform.scale(second_screen,(height,width)), (0, 0)) 
        pygame.display.flip()