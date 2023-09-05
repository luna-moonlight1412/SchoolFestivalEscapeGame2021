import pygame
import sys
from pygame.locals import*
import random

sys.path.append('../')
from crackingscreen import crackingscreen

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

COLOR=[(83,0,222),(83,0,222),(0,255,0)]

DOT=[[400,200],[500,200],[600,200],
     [400,300],[500,300],[600,300],
     [400,400],[500,400],[600,400]]

PASSCODE=[4,1,5,7,8]

BACK=[pygame.image.load("image/agent_back.png"),
      pygame.image.load("image/wrong_back.png"),
      pygame.image.load("image/agent_back.png")]

R=20 # Dot Size
L=30 # Carsor Range

index=0
tmr=0
x=0
y=0
mouse_c=0

col=0
passcode=[]

def init():
    global index,tmr,col,passcode
    index=1
    tmr=0
    col=0
    passcode=[]

def draw(bg):
    global tmr
    if col==1:
        rx=random.randint(-5,5)
        ry=random.randint(-5,5)
    else:
        rx=0
        ry=0
        
    bg.blit(BACK[col],[-5+rx,-5+ry])
    for i in range(9):
        pygame.draw.circle(bg,COLOR[col],(DOT[i][0]+rx,DOT[i][1]+ry),R)
    for i in range(len(passcode)-1):
        pygame.draw.line(bg,COLOR[col],(DOT[passcode[i]][0]+rx,DOT[passcode[i]][1]+ry),(DOT[passcode[i+1]][0]+rx,DOT[passcode[i+1]][1]+ry),5)

    if col==0 and len(passcode)>0:
        pygame.draw.line(bg,COLOR[0],(DOT[passcode[-1]][0],DOT[passcode[-1]][1]),(x,y),5)

def check():
    global passcode,col,tmr,index
    if mouse_c==1:
        for i in range(9):
            if DOT[i][0]-L<=x and x<=DOT[i][0]+L:
                if DOT[i][1]-L<=y and y<=DOT[i][1]+L:
                    if len(passcode)==0:
                        passcode.append(i)
                    elif len(passcode)>0:
                        if len(passcode)>1:
                            if passcode[-2]==i:
                                del passcode[-1]
                        if passcode[-1]!=i:
                            passcode.append(i)
    if mouse_c==0:
        if tmr>=20:
            if col==1:
                col=0
                passcode.clear()
            if col==2:
                index=2
                tmr=0
        if len(passcode)!=0 and tmr>=20:
            if passcode==PASSCODE:
                col=2
                tmr=0
            else:
                if len(passcode)!=1:
                    col=1
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
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,btn2,btn3=pygame.mouse.get_pressed()
        tmr+=1

        if index==0:
            init()
        if index==1:
            draw(screen)
            check()
        if index==2: 
            index=0
            ch=0
            crackingscreen.main(ch)
                    
        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
