import pygame
import sys
from pygame.locals import*
import os
import datetime
import pickle


WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

RET =  pygame.image.load("image/office/ret.png")
BACKS= [pygame.image.load("image/office/mail top.PNG"), 
        pygame.image.load("image/office/mail3.PNG"),
        pygame.image.load("image/office/mail1.PNG"),
        pygame.image.load("image/office/mail2.png"),
        pygame.image.load("image/office/mail4.5.png")]


index=0
tmr=0
x=0
y=0
mouse_c=0
check=0
num = 0

def init(bg):
    global index,num
    bg.fill(BLACK)
    index=0
    num=0
    ch=0
    with open('flg/office.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/init.binary','wb') as web:
        pickle.dump(ch,web)
    


def mail():
    global num

    if num != 0:
        if mouse_c == 1 :
                if 0<=x and x<=23:
                    if 0 <= y and y <= 36:
                        num = 0
    else:  
        for i in range(4):       
            if mouse_c==1 :
                if 30<=x and x<=889:
                    if 95 +104*i <= y and y <= 95 +104*(i+1):
                        num = i +1

def draw(bg):
    bg.fill(BLACK)
   
    for i in range(5):
        if num == i:
            bg.fill(WHITE)
            bg.blit(BACKS[i], (30, 0))
            if 1 <= i:
                bg.blit(RET, (0, 0))

                
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
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1
        tmr%=10

        if index==0: 
            if tmr==0:
                with open('flg/office.binary','rb') as web:
                    try:
                        index=pickle.load(web)
                    except:
                        pass
        if index==1:
            mail()
            draw(screen)
            check_i=0
            if tmr==0:
                with open('flg/init.binary','rb') as web:
                    try:
                        check_i=pickle.load(web)
                    except:
                        pass

            if check_i==1:
                init(screen)
       
        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
