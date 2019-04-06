from tg_gui import gui, system, system_handler
import pygame
from math import pi
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
print(dir(screen))

def color(r,g,b):
    return (r,g,b)

def round_rect(x, y, width, height, radius, color):
    pygame.draw.rect(screen, color, (x+radius ,y,width-radius*2,height), 0)
    pygame.draw.rect(screen, color, (x ,y+radius,width,height-radius*2), 0)
    pygame.draw.circle(screen, color, (x+radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+radius,y+height-radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+height-radius), radius, 0)

def text(*args, **kwargs):
    return

#setup gui
gui.color_max = 255
gui.color = color
gui.good_text_size = 1
gui.good_gap_size = 10
gui.good_widget_size = 100
gui.aprox_char_size = [7,10]
gui.round_rect = round_rect
gui.place_text = text

#setup system
system.x = 0
system.y = 0
system.width = 800
system.height = 600

system.init()

pygame.display.update()
    
while True:
    system.repl_query()
    print(system.cycle())
    
    pygame.display.update()
