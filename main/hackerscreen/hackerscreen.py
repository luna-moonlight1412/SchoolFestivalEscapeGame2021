import pygame
import sys
import os
from pygame.locals import*
import datetime

sys.path.append('../')
from tutorial import tutorialhacker
from stage1.hacking import hacker
from stage2.laboratory import laboratory_hacker
from stage3.changingpassword import hacker1,hacker2,hacker3


WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

PASS=["TUTO301","UDGE347","RKWX978","CSRU185","ZONE302","1981469"]

ipadd=""

index=0
tmr=0
x=0
y=0
mouse_c=0
col=0




BACK = pygame.transform.scale(pygame.image.load("image/hackerscreen/00.jpg"), (1020, 580))
LOGO = pygame.transform.scale(pygame.image.load("image/hackerscreen/kgs.png"), (256, 215))

def draw(bg,fnt, fnt2, fnt3):
    num = datetime.datetime.today()
    text1 = fnt2.render("Password", True, GREEN)
    text2 = fnt3.render("Welcome, intelligence.  Present your authority.", True, WHITE)
    date = fnt3.render(str(num), True, GREEN)


    bg.fill(BLACK)
    bg.blit(BACK, (0, 0))
    bg.blit(LOGO, (365, 330))

    pygame.draw.rect(bg,GREEN,[260,240,500,100],3)
    sur=fnt.render(ipadd,True,GREEN)
    bg.blit(sur,[270,250])

    bg.blit(text1, (360, 170))
    bg.blit(date, (370, 360))
    bg.blit(text2, (280, 500))



def password(key):
    global ipadd,tmr
    if key[K_RETURN]:
        if ipadd==PASS[0]:
            ipadd=""
            tutorialhacker.main()
        if ipadd==PASS[1]:
            ipadd=""
            hacker1.main()
        if ipadd==PASS[2]:
            ipadd=""
            hacker2.main()
        if ipadd==PASS[3]:
            ipadd=""
            hacker3.main()
        if ipadd==PASS[4]:
            ipadd=""
            hacker.main()
        if ipadd==PASS[5]:
            ipadd=""
            laboratory_hacker.main()

    if tmr>2:
        if key[K_BACKSPACE]:
            ipadd=ipadd[:-1]
            tmr=0
        if len(ipadd)<7:
            if key[K_0]:
                ipadd+="0"
                tmr=0
            elif key[K_1]:
                ipadd+="1"
                tmr=0
            elif key[K_2]:
                ipadd+="2"
                tmr=0
            elif key[K_3]:
                ipadd+="3"
                tmr=0
            elif key[K_4]:
                ipadd+="4"
                tmr=0
            elif key[K_5]:
                ipadd+="5"
                tmr=0
            elif key[K_6]:
                ipadd+="6"
                tmr=0
            elif key[K_7]:
                ipadd+="7"
                tmr=0
            elif key[K_8]:
                ipadd+="8"
                tmr=0
            elif key[K_9]:
                ipadd+="9"
                tmr=0
            elif key[K_a]:
                ipadd+="A"
                tmr=0
            elif key[K_b]:
                ipadd+="B"
                tmr=0
            elif key[K_c]:
                ipadd+="C"
                tmr=0
            elif key[K_d]:
                ipadd+="D"
                tmr=0
            elif key[K_e]:
                ipadd+="E"
                tmr=0
            elif key[K_f]:
                ipadd+="F"
                tmr=0
            elif key[K_g]:
                ipadd+="G"
                tmr=0
            elif key[K_h]:
                ipadd+="H"
                tmr=0
            elif key[K_i]:
                ipadd+="I"
                tmr=0
            elif key[K_j]:
                ipadd+="J"
                tmr=0
            elif key[K_k]:
                ipadd+="K"
                tmr=0
            elif key[K_l]:
                ipadd+="L"
                tmr=0
            elif key[K_m]:
                ipadd+="M"
                tmr=0
            elif key[K_n]:
                ipadd+="N"
                tmr=0
            elif key[K_o]:
                ipadd+="O"
                tmr=0
            elif key[K_p]:
                ipadd+="P"
                tmr=0
            elif key[K_q]:
                ipadd+="Q"
                tmr=0
            elif key[K_r]:
                ipadd+="R"
                tmr=0
            elif key[K_s]:
                ipadd+="S"
                tmr=0
            elif key[K_t]:
                ipadd+="T"
                tmr=0
            elif key[K_u]:
                ipadd+="U"
                tmr=0
            elif key[K_v]:
                ipadd+="V"
                tmr=0
            elif key[K_w]:
                ipadd+="W"
                tmr=0
            elif key[K_x]:
                ipadd+="X"
                tmr=0
            elif key[K_y]:
                ipadd+="Y"
                tmr=0
            elif key[K_z]:
                ipadd+="Z"
                tmr=0

def main():
    pygame.init()
    pygame.display.set_caption("PASS")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,120)
    font2 = pygame.font.Font(None,90)
    font3 = pygame.font.Font(None,30)

    while True:
        global tmr,mouse_c,x,y,col
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
            draw(screen,font, font2, font3)
            password(key)

        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
