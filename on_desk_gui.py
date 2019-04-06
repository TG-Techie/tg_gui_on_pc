from tg_gui import gui, system, system_handler
import pygame
from math import pi
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))

def color(r,g,b):
    return (r,g,b)

'''cur_surfs = []
def place_rect(x,y,width, height, color):
    surf = pygame.Surface((width, height))
    surf.fill(color)
    rect = surf.get_rect()
    screen.blit(surf, (x, y))
    

place_rect(0,0,30,50, color(255,128,96))

pygame.display.flip()
'''

def rounded_rect(x, y, width, height, radius, color):
    pygame.draw.rect(screen, color, (x+radius ,y,width-radius*2,height), 0)
    pygame.draw.rect(screen, color, (x ,y+radius,width,height-radius*2), 0)
    pygame.draw.circle(screen, color, (x+radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+radius,y+height-radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+height-radius), radius, 0)

def text(*args, **kwargs):
    return


print(dir(system))
    
while 1:
    system.query_repl()
    pygame.display.update()
