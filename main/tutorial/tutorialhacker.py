import pygame
import sys
from pygame.locals import*
import random

import hackerscreen

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

COLOR=(83,0,222)

DOT=[[400,200],[500,200],[600,200],
     [400,300],[500,300],[600,300],
     [400,400],[500,400],[600,400]]

PASSCODE=[4,1,5,7,8]

BACK=pygame.image.load("image/tutorial/hacker_back.png")

R=20 # Dot Size

index=0
tmr=0
x=0
y=0
mouse_c=0


def init():
    global index,tmr
    index=1
    tmr=0

def draw(bg):
    global tmr   
    bg.blit(BACK,[-5,-5])
    for i in range(9):
        pygame.draw.circle(bg,COLOR,(DOT[i][0],DOT[i][1]),R)
    if tmr<=10:
        pygame.draw.line(bg,COLOR,(500,300),(500,300-10*tmr),5)
    else:
        pygame.draw.line(bg,COLOR,(500,300),(500,200),5)
    if 10<=tmr<=20:
        pygame.draw.line(bg,COLOR,(500,200),(500+10*(tmr-10),200+10*(tmr-10)),5)
    elif 20<=tmr:
        pygame.draw.line(bg,COLOR,(500,200),(600,300),5)
    if 20<=tmr<=30:
        pygame.draw.line(bg,COLOR,(600,300),(600-10*(tmr-20),300+10*(tmr-20)),5)
    elif 30<=tmr:
        pygame.draw.line(bg,COLOR,(600,300),(500,400),5)
    if 30<=tmr<=40:
        pygame.draw.line(bg,COLOR,(500,400),(500+10*(tmr-30),400),5)
    elif 40<=tmr:
        pygame.draw.line(bg,COLOR,(500,400),(600,400),5)
    if tmr>=100:
        tmr=0
        
            
def main():
    pygame.init()
    pygame.display.set_caption("PASS")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,200)

    while True:
        global tmr,mouse_c,x,y,index
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((1020,580))
                if event.key==K_BACKSPACE or event.key==K_DELETE:
                    hackerscreen.main()
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            init()
        if index==1:
            draw(screen)
            
        if event.type==KEYDOWN:
            if event.key==K_F12:
                init()
                    
        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
