from tg_gui import gui, system, system_handler
import pygame, time
from math import pi
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.font.init()

def color(r,g,b):
    return (r,g,b)
5
def round_rect(x, y, width, height, radius, color):
    pygame.draw.rect(screen, color, (x+radius ,y,width-radius*2,height), 0)
    pygame.draw.rect(screen, color, (x ,y+radius,width,height-radius*2), 0)
    pygame.draw.circle(screen, color, (x+radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+radius), radius, 0)
    pygame.draw.circle(screen, color, (x+radius,y+height-radius), radius, 0)
    pygame.draw.circle(screen, color, (x+width-radius,y+height-radius), radius, 0)

def text(*args, **kwargs):
    return

def place_text(x, y, text, color = (255,255,255), background = (0,0,0),size = 1):
    for line in text.split('\n'):
        myfont = pygame.font.SysFont('Sans Serif', int(20*size))
        textsurface = myfont.render(line, False, color)
        screen.blit(textsurface,(x,y))
        y+= size*20
    
#setup gui
gui.color_max = 255
gui.color = color
gui.good_text_size = 1
gui.good_gap_size = 10
gui.good_widget_size = 100
gui.aprox_char_size = [5,20]
gui.round_rect = round_rect
gui.place_text = place_text

#setup system
system.x = 0
system.y = 0
system.width = 800
system.height = 600

#pygame.display.update()
#time.sleep(4000)


system.init()

should_loop = True
twas_pointed = False
pointer = 1
button = 2
mode = pointer
while should_loop:
    #system.repl_query()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            mode = button
            key =  event.key 
            if key == K_ESCAPE:
                running = False
            elif key == K_RETURN:
                system_handler.push_event('mv.prs')
            elif key == K_d or key==K_RIGHT:
                system_handler.push_event('mv.n')
            elif key == K_a or key == K_LEFT:
                system_handler.push_event('mv.p')
            elif key == K_h:
                system_handler.push_event('ld.h')
            elif key == K_s:
                system_handler.push_event('ld.s')
        elif event.type == QUIT:
            should_loop = False
    pointer_state = pygame.mouse.get_pressed()
    pointer_pos = pygame.mouse.get_pos()

    if pointer_state[0]:
        system_handler.push_event('ptr.g.'+str(pointer_pos).replace(' ',''),'ptr.d')
        twas_pointed = True
        mode = pointer
             
    else:
        if twas_pointed:
            system_handler.push_event('ptr.prs')
            twas_pointed = False
    if mode == pointer:
        system_handler.push_event('ptr.u')
    elif mode == button:
        system_handler.push_event('mv')

    
    ret = system.cycle()
    #if len(ret):
        #print(ret)
    pygame.display.update()

    if not should_loop:
        pygame.quit()
        break
