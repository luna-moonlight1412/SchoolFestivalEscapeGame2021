import pygame
import sys
from pygame.locals import*
import random
import os
import datetime
import pickle

import hackerscreen


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1020  #幅
HEIGHT = 580   #高さ
FPS = 30


Index = [0, 0, 0, 0, 100, 400, 250, 0]
Max_num = [168, 59, 130, 530, 530, 530, 530, 530]


def frame(screen, col, x, y, width, height, thick = 1):
    
    pygame.draw.lines(screen, col, True, [(x, y), (x, y +height), (x +width, y +height), (x +width, y)], thick)

    
def images(path, max_num):
    
    imgs = []
    
    for i in range(max_num):
        imgs.append(pygame.image.load(path + str(i) + ".png"))
        
    return imgs


def animation(imgs, wid_rate, hgt_rate, index_num, angle = 0):

    index = Index[index_num]
    image = imgs[index]

    image = pygame.transform.rotate(image, angle)
    
    x_size = image.get_width()  * wid_rate
    y_size = image.get_height() * hgt_rate
    image = pygame.transform.scale(image, (int(x_size), int(y_size)))

    return image


BACK = pygame.transform.scale(pygame.image.load("image/laboratory/image/trouble/back_3.png"), (WIDTH, HEIGHT))

noti_rate = 0.6
NOTI = [pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_1.png"), (int(1038*noti_rate), int(195*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_2.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_3.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_4.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_1f.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_2f.png"), (int(1039*noti_rate), int(336*noti_rate))), 
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/noti_3f.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/warning.png"), (int(1039*noti_rate), int(519*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/laboratory/image/notification/cons.png"), (int(1038*noti_rate), int(195*noti_rate)))]


wid_ind = 76
hgt_ind = 20

IND =pygame.transform.scale(pygame.image.load("image/laboratory/image/trouble/indicator.png"), (wid_ind, hgt_ind))
DNA =[]
for i in range(169):
    DNA.append(pygame.transform.scale(pygame.image.load("image/laboratory/movie ed png/VID-28/VID-28_"+str(i)+".png"),(500,580)))


color_bar = [(249, 36, 7), (246, 187, 0), (0, 164, 74), (0, 67, 200)]
y_bar = [45, 105, 165, 465]

PASS_T=[45,45,45,45]

index=0
tmr=0
tmr_d=0
tmr_c=0
x=0
y=0
mouse_c=0
trouble=0

            
def init():
    global passc,index,PASS_T
    index=1
    
    with open('../stage2/laboratory/flg/trouble/bar_pass.binary','rb') as web:
        PASS_T=pickle.load(web)

    
def draw(bg):
    global check,date2,index,y_bar,PASS_T,trouble,tmr_c
    if tmr==0:
        with open('../stage2/laboratory/flg/trouble/trouble.binary','rb') as web:
            try:
                trouble=pickle.load(web)
            except:
                pass

    
    if trouble!=7:
        bg.fill(BLACK)
        bg.blit(DNA[tmr_d],[0,0])
        bg.blit(DNA[(tmr_d+90)%169],[520,0])
        bg.blit(NOTI[trouble], (170, 120))
        tmr_c=0
    if trouble==7:
        bg.fill(WHITE)
        bg.blit(BACK, (0,0))
        for i in range(4):
            pygame.draw.rect(bg, color_bar[i], (200 +185*i, y_bar[i], 66, 422-(y_bar[i] -45)))
            bg.blit(IND, [194 +185*i, y_bar[i] -15])
            pygame.draw.line(bg, BLACK, (200 +185*i, PASS_T[i]+15),(266+185*i,PASS_T[i]+15),5)
            pygame.draw.line(bg, BLACK, (200 +185*i, PASS_T[i]-15),(266+185*i,PASS_T[i]-15),5)
        if tmr_c<=70:
            bg.blit(NOTI[trouble], (170, 120))
        

    if tmr==0:
        with open('../stage2/laboratory/flg/trouble/bar.binary','rb') as web:
            try:
                y_bar=pickle.load(web)
            except:
                pass
        with open('../stage2/laboratory/flg/trouble/bar_pass.binary','rb') as web:
            try:
                PASS_T=pickle.load(web)
            except:
                pass

            
            
def main():
    
    pygame.init()
    pygame.display.set_caption("PASS")
    screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
    
    clock = pygame.time.Clock()

    while True:
        global tmr,mouse_c,x,y,col,check,date2,tmr_d,tmr_c
    
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
        tmr%=5
        tmr_d+=1
        tmr_d%=169
        tmr_c+=1
        

        if index == 0:
            init()
        if index == 1:
            draw(screen)
              
        pygame.display.update()
        clock.tick(FPS)


if __name__=='__main__':
    main()
