import pygame
import sys
from pygame.locals import*
import pickle

BLACK=(0,0,0)
GREEN=(0,255,0)

index=0
tmr=0
x=0
y=0
mouse_c=0

ch1=0
ch2=0
ch3=0
ch4=0
ch5=0
ch6=0

def p_init():
    global index,ch1,ch2,ch3,ch4,ch5,ch6
    ch1=0
    ch2=0
    ch3=0
    ch4=0
    ch5=0
    ch6=0
    index=1
    
    ch=0
    with open('../crackingscreen/flg/init_tuto.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_dial.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../stage1/hacking/flg/init.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../stage2/laboratory/flg/init.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_1.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_2.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_3.binary','wb') as web:
        pickle.dump(ch,web)

def init():
    global index
    ch=1
    with open('../crackingscreen/flg/init_tuto.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_dial.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../stage1/hacking/flg/init.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../stage2/laboratory/flg/init.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_1.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_2.binary','wb') as web:
        pickle.dump(ch,web)
    with open('../crackingscreen/flg/init_stage3_3.binary','wb') as web:
        pickle.dump(ch,web)

    ch=0
    with open('flg/stage1_1.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/stage1_2.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/stage2.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/stage3_1.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/stage3_2.binary','wb') as web:
        pickle.dump(ch,web)
    with open('flg/stage3_3.binary','wb') as web:
        pickle.dump(ch,web)
    index=1

def draw(bg,fnt1,fnt2):
    global ch1,ch2,ch3,ch4,ch5,ch6
    bg.fill(BLACK)
    pygame.draw.rect(bg,GREEN,[100,50,250,200])
    pygame.draw.rect(bg,GREEN,[385,50,250,200])
    pygame.draw.rect(bg,GREEN,[670,50,250,200])
    pygame.draw.rect(bg,GREEN,[100,300,250,200])
    pygame.draw.rect(bg,GREEN,[385,300,250,200])
    pygame.draw.rect(bg,GREEN,[670,300,250,200])
    pygame.draw.rect(bg,BLACK,[105,100,240,145])
    pygame.draw.rect(bg,BLACK,[390,100,240,145])
    pygame.draw.rect(bg,BLACK,[675,100,240,145])
    pygame.draw.rect(bg,BLACK,[105,350,240,145])
    pygame.draw.rect(bg,BLACK,[390,350,240,145])
    pygame.draw.rect(bg,BLACK,[675,350,240,145])
    
    sur=fnt1.render("STAGE1(PC)",True,BLACK)
    bg.blit(sur,[130,60])
    sur=fnt1.render("STAGE1(DIAL)",True,BLACK)
    bg.blit(sur,[395,60])
    sur=fnt1.render("STAGE2",True,BLACK)
    bg.blit(sur,[710,60])
    sur=fnt1.render("STAGE3-1",True,BLACK)
    bg.blit(sur,[140,310])
    sur=fnt1.render("STAGE3-2",True,BLACK)
    bg.blit(sur,[425,310])
    sur=fnt1.render("STAGE3-3",True,BLACK)
    bg.blit(sur,[710,310])
    
    if tmr==0:
        with open('flg/stage1_1.binary','rb') as web:
            ch1=pickle.load(web)
        with open('flg/stage1_2.binary','rb') as web:
            ch2=pickle.load(web)
        with open('flg/stage2.binary','rb') as web:
            try:
                ch3=pickle.load(web)
            except:
                pass
        with open('flg/stage3_1.binary','rb') as web:
            try:
                ch4=pickle.load(web)
            except:
                pass
        with open('flg/stage3_2.binary','rb') as web:
            ch5=pickle.load(web)
        with open('flg/stage3_3.binary','rb') as web:
            ch6=pickle.load(web)

    if ch1==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[130,150])
    if ch2==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[415,150])
    if ch3==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[700,150])
    if ch4==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[130,400])
    if ch5==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[415,400])
    if ch6==1:
        sur=fnt1.render("COMPLETE",True,GREEN)
        bg.blit(sur,[700,400])

    
    

def main():
    pygame.init()
    pygame.display.set_caption("")
    screen=pygame.display.set_mode((1020,580))
    clock=pygame.time.Clock()
    font1=pygame.font.Font(None,50)
    font2=pygame.font.Font(None,80)

    while True:
        global index,tmr,x,y,mouse_c
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F1:
                    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
                if event.key==K_ESCAPE:
                    screen=pygame.display.set_mode((1020,580))
                if event.key==K_F12:
                    init()
        key=pygame.key.get_pressed()
        x,y=pygame.mouse.get_pos()
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1
        tmr%=30

        if index==0:
            p_init()
        if index==1:
            draw(screen,font1,font2)
        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
