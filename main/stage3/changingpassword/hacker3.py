import pygame
import sys
from pygame.locals import*
import random
import datetime

import hackerscreen

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

CODE=[]
for i in range(1,31):
    CODE.append(pygame.image.load("image/changingpassword/image/3 screen/"+str(i)+'.png'))
    
PASS=[[4, 2], [0, 1], [1, 5], [2, 4], [5, 4], [3, 0], [3, 2], [0, 3], [4, 3], [4, 1], [5, 2], [4, 0], [0, 4], [1, 0], [0, 5], [2, 1], [1, 3], [2, 0], [5, 1], [0, 2], [3, 1], [2, 3], [1, 2], [5, 0], [1, 4], [3, 4], [4, 5], [5, 3], [3, 5], [2, 5]]

TIME=20 #制限時間
COMB=6 #通り数

index=0
tmr=0
x=0
y=0
mouse_c=0
change=0
flg=0


def draw(bg,time):
    global flg,tmr
    bg.fill(WHITE)
    if flg==1:
        bg.fill(WHITE)
        bg.blit(pygame.transform.scale(CODE[time],[102+tmr*63,58+tmr*36]),[918-tmr*63,522-tmr*36])
    if tmr>=15:
        bg.blit(CODE[time],[0,0])
                            
   
def main():
    pygame.init()
    pygame.display.set_caption("PASS")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,200)

    while True:
        global tmr,mouse_c,x,y,change,flg
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
            date=datetime.datetime.now()
            time=int((date.hour*3600+date.minute*60+date.second)%(TIME*len(PASS))/TIME)
            if change!=time:
                change=time
                flg=1
                tmr=0
            draw(screen,time)

        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
