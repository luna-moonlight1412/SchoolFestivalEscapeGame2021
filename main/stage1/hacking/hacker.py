import pygame
import sys
from pygame.locals import*
import random
import os
import datetime
import pickle
import time


import hackerscreen
sys.path.append('../')
from crackingscreen import crackingscreen


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1020  #幅
HEIGHT = 580   #高さ
FPS = 30


#--背景設定----------------------------------------------------------------------------

Index = [0, 0, 0, 0, 40, 120]
Max_num = [108, 67, 452, 228, 228, 228]


def frame(screen, col, x, y, width, height, thick = 1):
    
    pygame.draw.lines(screen, col, True, [(x, y), (x, y +height), (x +width, y +height), (x +width, y)], thick)

    
def images(path, max_num):
    
    imgs = []
    
    for i in range(max_num):
        imgs.append(pygame.image.load(path + str(i) + ".png"))
        
    return imgs


def animation(imgs,  wid_rate, hgt_rate, index_num):

    index = Index[index_num]
    image = imgs[index]
            
    x_size = image.get_width()  * wid_rate
    y_size = image.get_height() * hgt_rate
    image = pygame.transform.scale(image, (int(x_size), int(y_size)))

    return image


BACK = pygame.transform.scale(pygame.image.load("image/hacking/image/back.png"), (WIDTH, HEIGHT))
NEXT=pygame.image.load("image/hacking/image/next.png")

NETWORK = images("image/hacking/movie/movie ed png/VID-1/VID-1_", Max_num[0])
PROGRAM = images("image/hacking/movie/movie ed png/VID-5/VID-5_", Max_num[1])
TRANSITION = images("image/hacking/movie/movie ed png/VID-17/VID-17_", Max_num[2])
LOADING1 = images("image/hacking/movie/movie ed png/VID-20/VID-20_", Max_num[3])
LOADING2 = images("image/hacking/movie/movie ed png/VID-20/VID-20_", Max_num[4])
LOADING3 = images("image/hacking/movie/movie ed png/VID-20/VID-20_", Max_num[5])



#--ゲーム設定--------------------------------------------------------------------------


NUM =[[pygame.image.load("image/hacking/image/number/0.png"),
       pygame.image.load("image/hacking/image/number/1.png")],
      [pygame.image.load("image/hacking/image/number/0r.png"),
       pygame.image.load("image/hacking/image/number/1r.png")]]


PASS=[[[2,2,2,2,2,2,2],
       [2,1,1,1,1,1,2],
       [2,1,0,0,0,1,2],
       [2,1,0,1,0,1,2],
       [2,1,0,0,0,1,2],
       [2,1,1,1,1,1,2],
       [2,2,2,2,2,2,2]],
      
      [[2,2,2,2,2,2,2],
       [2,1,1,0,1,1,2],
       [2,1,1,0,1,1,2],
       [2,0,0,0,0,0,2],
       [2,1,1,0,1,1,2],
       [2,1,1,0,1,1,2],
       [2,2,2,2,2,2,2]],

      [[2,2,2,2,2,2,2],
       [2,1,0,0,0,1,2],
       [2,0,1,0,1,0,2],
       [2,0,0,1,0,0,2],
       [2,0,1,0,1,0,2],
       [2,1,0,0,0,1,2],
       [2,2,2,2,2,2,2]]]


COUNT = [1,2,2]


index=0
tmr=0
x=0
y=0
mouse_c=0
col=0
check=1
date2=0
level=0
cnt=0
level_c=0
wrong=0


passw=[[2,2,2,2,2,2,2],
       [2,1,1,1,1,1,2],
       [2,1,0,0,0,1,2],
       [2,1,0,1,0,1,2],
       [2,1,0,0,0,1,2],
       [2,1,1,1,1,1,2],
       [2,2,2,2,2,2,2]]


def reverse(r1,r2):
    for i in range(-1,2):
        for j in range(-1,2):
            if passw[r2+i][r1+j] == 0:
                passw[r2+i][r1+j] = 1
            elif passw[r2+i][r1+j] == 1:
                passw[r2+i][r1+j] = 0
            else:
                pass

            
def init():
    global passw,index,col,check,level,cnt,leve_c,wrong
    passw=[[2,2,2,2,2,2,2],
           [2,1,1,1,1,1,2],
           [2,1,0,0,0,1,2],
           [2,1,0,1,0,1,2],
           [2,1,0,0,0,1,2],
           [2,1,1,1,1,1,2],
           [2,2,2,2,2,2,2]]
    
    r1=random.randint(1,5)
    r2=random.randint(1,5)
    reverse(r1,r2)
    col=0
    check=1
    level=0
    cnt=0
    level_c=0
    wrong=0
    index=1

    
def draw(bg, fnt1, fnt2,fnt3):
    global check,date2,index
    
    bg.fill(BLACK)
    if check == 1:

        Text1 = fnt1.render("Locked", True, RED)
        
        text1 = fnt2.render("System1 :", True, WHITE)
        text2 = fnt2.render("System2 :", True, WHITE)
        text3 = fnt2.render("System3 :", True, WHITE)
        text4 = fnt2.render("System4 :", True, WHITE)
        text5 = fnt2.render("System5 :", True, WHITE)
        text6 = fnt2.render("System6 :", True, WHITE)

        title1 = fnt3.render("Hacking Tools", True, GREEN)
        title2_1 = fnt3.render("Network", True, GREEN)
        title2_2 = fnt3.render("Optimizer", True, GREEN)
        title3_1 = fnt3.render("System", True, GREEN)
        title3_2 = fnt3.render("Database", True, GREEN)
        title4 = fnt3.render("S.C.P Files", True, GREEN)
        
        bg.blit(BACK, (0,0))
        
        bg.blit(animation(NETWORK, 1, 1, 0), (3, 431))
        bg.blit(animation(PROGRAM, 1, 1, 1), (4, 131))
        bg.blit(animation(TRANSITION, 1, 1, 2), (286, 445))        
        bg.blit(animation(LOADING3, 1, 1, 5), (825, 35))
        bg.blit(animation(LOADING2, 1, 1, 4), (825, 75))
        bg.blit(animation(LOADING1, 1, 1, 3), (825, 115))
        bg.blit(animation(LOADING3, 1, 1, 5), (825, 155))
        bg.blit(animation(LOADING2, 1, 1, 4), (825, 195))
        bg.blit(animation(LOADING1, 1, 1, 3), (825, 235))

        frame(bg, RED, 32, 42, 215, 65, 4)
        bg.blit(Text1, [50, 52])

        bg.blit(text1, [725, 35])
        bg.blit(text2, [725, 75])
        bg.blit(text3, [725, 115])
        bg.blit(text4, [725, 155])
        bg.blit(text5, [725, 195])
        bg.blit(text6, [725, 235])

        bg.blit(title1, [943, 49])
        bg.blit(title2_1, [943, 136])
        bg.blit(title2_2, [943, 146])
        bg.blit(title3_1, [943, 222])
        bg.blit(title3_2, [943, 232])
        bg.blit(title4, [943, 313])


        for i in range(len(Index)):

            Index[i] += 1
            Index[i] %= Max_num[i]

               
    for i in range(1,6):
        for j in range(1,6):
            if level_c == 1:
                bg.blit(pygame.transform.scale(NUM[0][passw[j][i]], [30,35]), [i*40+670, j*40+295])
            else:
                bg.blit(pygame.transform.scale(NUM[0][PASS[level][j][i]], [30,35]), [i*40+670, j*40+295])
                
            bg.blit(pygame.transform.scale(NUM[wrong][passw[j][i]], [60,70]), [i*70+245, j*70-30])

    if level_c==1:
        if -40<=tmr and tmr<-20:
            nexts=NEXT.subsurface((int(150-(tmr+40)*7.5),0,(tmr+40)*15,90))
            bg.blit(nexts,[490-(tmr+40)*7.5,170])
        if -20<=tmr and tmr<-10:
            nexts=NEXT
            bg.blit(nexts,[340,170])
        if tmr>=-10:
            nexts=NEXT.subsurface(((tmr+10)*15,0,300-(tmr+10)*30,90))
            bg.blit(nexts,[340+(tmr+10)*15,170])


def game():
    global level,cnt,tmr,index,level_c,wrong
    
    if mouse_c == 1 and tmr > 10:
        for i in range(1,6):
            for j in range(1,6):
                if i*70+245 < x and x < i*70+305:
                    if j*70-30 < y and y < j*70+40:
                        cnt += 1
                        tmr = 0
                        reverse(i,j)
  
    if tmr > 0:
        if passw == PASS[level]:
            if level != 2:
                level_c = 1
                cnt = 0
                tmr = -40
            else:
                index = 2
                
        if passw != PASS[level] and cnt == COUNT[level]:
            tmr = -40
            cnt = 0
            wrong=1

    if -10 < tmr and tmr < -1:
        for i in range(1,6):
            for j in range(1,6):
                passw[i][j] = random.randint(0,1)


    if tmr == -1:
        wrong=0
        if level_c == 1:
            level += 1
            level_c = 0
        for i in range(7):
            for j in range(7):
                passw[i][j] = PASS[level][i][j]
                
        if level == 0:
            r1 = random.randint(1,5)
            r2 = random.randint(1,5)
            reverse(r1,r2)
            
        if level == 1:
            r1 = random.randint(1,5)
            r2 = random.randint(1,5)
            reverse(r1,r2)
            r3 = random.randint(1,5)
            r4 = random.randint(1,5)
            while r3 == r1 and r4 == r2:
                r3 = random.randint(1,5)
                r4 = random.randint(1,5)
            reverse(r3,r4)
            
        if level == 2:
            r1 = random.randint(1,5)
            r2 = random.randint(1,5)
            reverse(r1,r2)
            r3 = random.randint(2,4)
            r4 = random.randint(2,4)
            while r3 == r1 and r4 == r2:
                r3 = random.randint(2,4)
                r4 = random.randint(2,4)
            reverse(r3,r4)

            
def main():
    
    pygame.init()
    pygame.display.set_caption("PASS")
    screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
    
    clock = pygame.time.Clock()
    font1 = pygame.font.Font(None, 75)
    font2 = pygame.font.Font(None, 25)
    font3 = pygame.font.Font(None, 15)


    while True:
        global tmr,mouse_c,x,y,col,check,date2,index
    
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen=pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((WIDTH,HEIGHT))
                if event.key==K_BACKSPACE or event.key==K_DELETE:
                    hackerscreen.main()
                    
        key = pygame.key.get_pressed()
        x,y = pygame.mouse.get_pos()
        mouse_c,btn2,btn3 = pygame.mouse.get_pressed()
        tmr+=1
        

        
        if index == 0:
            init()
        if index == 1:
            draw(screen, font1, font2,font3)
            game()
        if index==2:
            ch=1
            with open('../stage1/hacking/flg/office.binary','wb') as web:
                pickle.dump(ch,web)
            with open('../progress/flg/stage1_1.binary','wb') as web:
                pickle.dump(ch,web)
            init()
            ch=5
            crackingscreen.main(ch)
      
        pygame.display.update()
        clock.tick(FPS)


if __name__=='__main__':
    main()
