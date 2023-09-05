import pygame
import sys
from pygame.locals import*
import random
import datetime
import pickle

sys.path.append('../../')
from crackingscreen import crackingscreen

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)

BACK=[pygame.image.load("image/back/agent back1.png"),
      pygame.image.load("image/back/agent back2.png")]

BUTTON=[pygame.image.load("image/button/lock.png"),
        pygame.image.load("image/button/open.png")]

CODE=[[pygame.image.load("image/2/1.png"),
       pygame.image.load("image/2/2.png"),
       pygame.image.load("image/2/3.png"),
       pygame.image.load("image/2/4.png"),
       pygame.image.load("image/2/5.png"),
       pygame.image.load("image/2/6.png")]]

COORDINATE=[[35,140],[370,140],[700,140],
            [35,355],[370,355],[700,355]]

COORDINATE_I=[[50,190],[385,190],[715,190],
              [50,400],[385,400],[715,400]]

COORDINATE_B=[[215,220],[550,220],[880,220],
              [215,430],[550,430],[880,430]]

PASS=[[[2, 3], [1, 2], [5, 4], [4, 1], [5, 2], [4, 0], [2, 1], [0, 2], [1, 5], [0, 3], [5, 0], [3, 4], [1, 4], [3, 0], [1, 3], [4, 5], [4, 3], [4, 2], [3, 2], [2, 0], [3, 5], [2, 5], [1, 0], [5, 3], [3, 1], [0, 4], [5, 1], [2, 4], [0, 5], [0, 1]]]

TIME=20 #制限時間
COMB=6 #通り数
cooltime=40 #クールタイム

index=0
tmr=0
tmr_i=0
x=0
y=0
mouse_c=0
c_time=0
change=0
cnt=0

color=0
passw=[]
lock=[0,0,0,0,0,0]

def init():
    global index,tmr,c_time,change,color,passw,lock,cnt
    index=1
    tmr=0
    c_time=0
    change=0
    color=0
    cnt=0
    passw.clear()
    for i in range(6):
        lock[i]=0

def draw(bg,fnt,fnts):
    if color==1:
        rx=random.randint(-5,5)
        ry=random.randint(-5,5)
    else:
        rx=0
        ry=0

    if color==0:
        bg.blit(BACK[color],[0,0])
    else:
        bg.blit(BACK[color],[-5+rx,-5+ry])
        
    for i in range(6):
        bg.blit(CODE[0][i],[COORDINATE_I[i][0]+rx,COORDINATE_I[i][1]+ry])
        bg.blit(BUTTON[lock[i]],[COORDINATE_B[i][0]+rx,COORDINATE_B[i][1]+ry])
    sur=fnts.render("ENTER PASSCODE "+str(cnt)+"/2",True,GREEN)
    bg.blit(sur,[45,45])
        
    if -cooltime<=tmr and tmr<0:
        surface_a=pygame.Surface((1020,580))
        surface_a.fill(BLACK)
        surface_a.set_alpha(150)
        bg.blit(surface_a,[0,0])
        
        sur=fnt.render("Now Loading...",True,WHITE)
        bg.blit(sur,[270,230])
        pygame.draw.rect(bg,WHITE,[270,320,490*((cooltime+tmr)/cooltime),50])
        
        

def check(time):
    global passw,color,tmr,index,c_time,lock,cnt
    if tmr>=-cooltime:
        color=0
    if mouse_c==0:
        c_time=0
    if mouse_c==1 and tmr>30:
        for i in range(6):
            if COORDINATE[i][0]<=x and x<=COORDINATE[i][0]+290:
                if COORDINATE[i][1]<=y and y<=COORDINATE[i][1]+190:
                    if len(passw)==0 and c_time>=40:
                        if PASS[0][time][0]==i:
                            passw.append(i)
                            c_time=0
                            tmr=0
                            cnt=1
                            lock[i]=1
                        else:
                            c_time=0
                            tmr=-cooltime-30
                            color=1
                            passw.clear()
                            for i in range(6):
                                lock[i]=0
                            cnt=0
                    elif len(passw)==1 and c_time>=40:
                        if PASS[0][time][1]==i:
                            index=2
                            tmr=0
                            cnt=2
                            lock[i]=1
                        else:
                            c_time=0
                            tmr=-cooltime-30
                            color=1
                            passw.clear()
                            for i in range(6):
                                lock[i]=0
                            cnt=0
        c_time+=1
                            

def cursor(bg):
    if 0<c_time and c_time<=40 and color!=1:
        for i in range(6):
            if COORDINATE[i][0]<=x and x<=COORDINATE[i][0]+290:
                if COORDINATE[i][1]<=y and y<=COORDINATE[i][1]+190:
                    pygame.draw.arc(bg,GREEN,[x-25,y-25,50,50],0,6.28*c_time/40,5)
            
def main():
    pygame.init()
    pygame.display.set_caption("PASS")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,100)
    fonts=pygame.font.Font(None,50)

    while True:
        global tmr,mouse_c,x,y,change,passw,cnt,index,lock,tmr_i
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
        tmr_i+=1
        tmr_i%=10

        if index==0:
            init()

        if index==1:
            date=datetime.datetime.now()
            time=int((date.hour*3600+date.minute*60+date.second)%(TIME*len(PASS[0]))/TIME)
            if change!=time:
                passw.clear()
                cnt=0
                for i in range(6):
                    lock[i]=0
            change=time
            draw(screen,font,font)
            check(time)
            cursor(screen)

        if index==2:
            index=0
            ch=1
            with open('../../progress/flg/stage3_2.binary','wb') as web:
                pickle.dump(ch,web)
            ch=2
            crackingscreen.main(ch)

        check_i=0
        if tmr_i==0:
            with open('../../crackingscreen/flg/init_stage3_2.binary','rb') as web:
                try:
                    check_i=pickle.load(web)
                except:
                    pass
        if check_i==1:
            ch=0
            with open('../../crackingscreen/flg/init_stage3_2.binary','wb') as web:
                pickle.dump(ch,web)
            init()

        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
