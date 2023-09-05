import pygame
import sys
from pygame.locals import*
from importlib import import_module
import pickle

modules = ['tutorialagent', 'dial', 'agent1', 'agent2', 'agent3', 'hackerscreen']
MODU = [0, 0, 0, 0, 0, 0]
for i in range(6):
    try:
        MODU[i] = import_module(modules[i])
    except:
        pass

BLACK=(0,0,0)
ALPH=['c','o','m','p','l','e','t']

Back = pygame.image.load("image/crackingscreen/image/back.png")
ALPHABET=[]
for i in range(7):
    ALPHABET.append(pygame.image.load("image/crackingscreen/image/alphabet/"+ALPH[i]+".png"))

index=0
tmr=0
tmr_i=0
x=0
y=0
mouse_c=0
check=0

def crack_screen(bg):
    global tmr,index
    bg.fill(BLACK)
    bg.blit(Back,[0,0-tmr*100])
    if tmr>=68:
        tmr=0
        index=1

def complete(bg):
    global tmr,index
    bg.fill(BLACK)
    if tmr>=1:
        bg.blit(ALPHABET[0],[40,230])
    else:
        bg.blit(ALPHABET[0],[56*tmr,230])
    if tmr>=2:
        bg.blit(ALPHABET[1],[145,230])
    else:
        bg.blit(ALPHABET[1],[56*tmr,230])
    if tmr>=3:
        bg.blit(ALPHABET[2],[230,230])
    else:
        bg.blit(ALPHABET[2],[56*tmr,230])
    if tmr>=6:
        bg.blit(ALPHABET[3],[380,230])
    else:
        bg.blit(ALPHABET[3],[56*tmr,230])
    if tmr>=8:
        bg.blit(ALPHABET[4],[480,230])
    else:
        bg.blit(ALPHABET[4],[56*tmr,230])
    if tmr>=10:
        bg.blit(ALPHABET[5],[595,230])
    else:
        bg.blit(ALPHABET[5],[56*tmr,230])
    if tmr>=13:
        bg.blit(ALPHABET[6],[735,230])
    else:
        bg.blit(ALPHABET[6],[56*tmr,230])
    if tmr>=14:
        bg.blit(ALPHABET[5],[830,230])
    else:
        bg.blit(ALPHABET[5],[56*tmr,230])
    if tmr>=30:
        index=2

def back_game(key,check):
    global tmr,index
    if tmr_i==0:
        CH1=0 #agent1
        CH2=0 #agent2
        CH3=0 #agent3
        CH4=0 #dial
        try:
            with open('../../crackingscreen/flg/init_stage3_1.binary','rb') as web:
                CH1=pickle.load(web)
        except:
            pass
        try:
            with open('../../crackingscreen/flg/init_stage3_2.binary','rb') as web:
                CH2=pickle.load(web)
        except:
            pass
        try:
            with open('../../crackingscreen/flg/init_stage3_3.binary','rb') as web:
                CH3=pickle.load(web)
        except:
            pass
        try:
            with open('../../crackingscreen/flg/init_dial.binary','rb') as web:
                CH4=pickle.load(web)
        except:
            pass

        ch=0
        if CH1==1 and check==1:
            tmr=0
            index=0
            with open('../../crackingscreen/flg/init_stage3_1.binary','wb') as web:
                pickle.dump(ch,web)
            MODU[2].main()
        if CH2==1 and check==2:
            tmr=0
            index=0
            with open('../../crackingscreen/flg/init_stage3_2.binary','wb') as web:
                pickle.dump(ch,web)
            MODU[3].main()
        if CH3==1 and check==3:
            tmr=0
            index=0
            with open('../../crackingscreen/flg/init_stage3_3.binary','wb') as web:
                pickle.dump(ch,web)
            MODU[4].main()
        if CH4==1 and check==4:
            tmr=0
            index=0
            with open('../../crackingscreen/flg/init_dial.binary','wb') as web:
                pickle.dump(ch,web)
            MODU[1].main()


    if key[K_F12]:
        if check==0:
            tmr=0
            index=0
            MODU[0].main()
        if check==5:
            tmr=0
            index=0
            MODU[5].main()

def main(check):
    pygame.init()
    pygame.display.set_caption("")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()

    while True:
        global index,tmr,x,y,mouse_c,index,tmr_i
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
        mouse_c,b1,b2=pygame.mouse.get_pressed()
        tmr+=1
        tmr_i+=1
        tmr_i%=10

        if index==0:
            crack_screen(screen)
        if index==1:
            complete(screen)
        if index==2:
            back_game(key,check)


        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main(check)
