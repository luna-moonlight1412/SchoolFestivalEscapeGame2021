import pygame
import sys
from pygame.locals import*
import random
import os
import datetime
import pickle


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1020  #幅
HEIGHT = 580   #高さ
FPS = 30


#--背景設定----------------------------------------------------------------------------

Index = [0, 0, 0, 0, 100, 400, 250, 0]
Max_num = [168, 59, 300, 530, 530, 530, 530, 530]


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


BACK = pygame.transform.scale(pygame.image.load("image/back.png"), (WIDTH, HEIGHT))

DNA = images("movie ed png/VID-28/VID-28_", Max_num[0])
DNA_CODE = images("movie ed png/VID-27/VID-27_", Max_num[1])
CHROMAT = images("movie ed png/VID-30/VID-30_", Max_num[2])

noti_rate = 0.6
NOTI = [pygame.transform.scale(pygame.image.load("image/notification/noti_1.png"), (int(1038*noti_rate), int(195*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/noti_2.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/noti_3.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/noti_4.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/noti_1f.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/noti_2f.png"), (int(1039*noti_rate), int(336*noti_rate))), 
        pygame.transform.scale(pygame.image.load("image/notification/noti_3f.png"), (int(1039*noti_rate), int(336*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/warning.png"), (int(1039*noti_rate), int(519*noti_rate))),
        pygame.transform.scale(pygame.image.load("image/notification/cons.png"), (int(1038*noti_rate), int(195*noti_rate)))]


LAMP = [pygame.image.load("image/lamp/lampA-min.png"),
        pygame.image.load("image/lamp/lampB-min.png"),
        pygame.image.load("image/lamp/lampC-min.png"),
        pygame.image.load("image/lamp/lampD-min.png")]


BAR = [pygame.image.load("image/bar/bar0-min.png"),
       pygame.image.load("image/bar/bar1-min.png"),
       pygame.image.load("image/bar/bar2-min.png"),
       pygame.image.load("image/bar/bar3-min.png"),
       pygame.image.load("image/bar/bar4-min.png")]


BACK_T = pygame.transform.scale(pygame.image.load("image/trouble/back_3.png"), (WIDTH, HEIGHT))
IND =pygame.image.load("image/trouble/indicator.png")

RET =  pygame.image.load("image/result/ret.png")


Virus_vc = [pygame.image.load("image/virus/2.png"),
            pygame.image.load("image/virus/17.png")]
        
Result_vc = [[pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-d.jpg"), pygame.image.load("image/result/VP-13.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-d.jpg"), pygame.image.load("image/result/VP-13.jpg"), pygame.image.load("image/result/VP-15.jpg")]]

Virus_vr = [pygame.image.load("image/virus/1.png"),
            pygame.image.load("image/virus/3.png"),
            pygame.image.load("image/virus/4.png"),
            pygame.image.load("image/virus/5.png"),
            pygame.image.load("image/virus/6.png"),
            pygame.image.load("image/virus/7.png"),
            pygame.image.load("image/virus/8.png"),
            pygame.image.load("image/virus/9.png"),
            pygame.image.load("image/virus/10.png"),
            pygame.image.load("image/virus/11.png"),
            pygame.image.load("image/virus/12.png"),
            pygame.image.load("image/virus/13.png"),
            pygame.image.load("image/virus/14.png"),
            pygame.image.load("image/virus/15.png"),
            pygame.image.load("image/virus/16.png")]

Result_vr = [[pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-a.jpg"), pygame.image.load("image/result/VP-1.jpg"), pygame.image.load("image/result/VP-2.jpg")], 
             [pygame.image.load("image/result/20.png"), pygame.image.load("image/result/DNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-100.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-a.jpg"), pygame.image.load("image/result/VP-10.jpg"), pygame.image.load("image/result/VP-6.jpg")],
             [pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/20.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-a.jpg"), pygame.image.load("image/result/VP-1.jpg"), pygame.image.load("image/result/VP-2.jpg")],
             [pygame.image.load("image/result/8.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-100.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/4.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-12.jpg"), pygame.image.load("image/result/VP-10.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/4.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-a.jpg"), pygame.image.load("image/result/VP-10.jpg"), pygame.image.load("image/result/VP-6.jpg")],
             [pygame.image.load("image/result/4.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-100.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/egg.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-50.jpg"), pygame.image.load("image/result/VP-51.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/egg.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/VP-30.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/str.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/MP-1.png"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/str.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/MP-2.png"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/bar.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")],
             [pygame.image.load("image/result/bar.png"), pygame.image.load("image/result/RNA.jpg"), pygame.image.load("image/result/NP.jpg"), pygame.image.load("image/result/GP-b.jpg"), pygame.image.load("image/result/blank.jpg"), pygame.image.load("image/result/blank.jpg")]]

Back_file = pygame.image.load("image/result/Files.png")
DRAWS = [Result_vc[0], Result_vc[1]]
DRAWS_2 = [Virus_vc[0], Virus_vc[1]]

rans = random.sample(range(len(Result_vr)), 2)
for i in range(2):
    DRAWS.insert(1, Result_vr[rans[i]])
for i in range(2):
    DRAWS_2.insert(1, Virus_vr[rans[i]])
        
#---------------------------------------------

PASS=[[0,[0,1,2,3]],
      [0,[0,1,2,3]],
      [0,[0,1,2,3]]]

PASS_T=[45,45,45,45]

det = [0, 0, 0]
noti = 0

color_bar = [(249, 36, 7), (246, 187, 0), (0, 164, 74), (0, 67, 200)]
y_bar = [45, 105, 165, 465]

index=0
tmr=0
tmr_l=0
tmr_i=0
x=0
y=0
mouse_c=0
level=0
btn=-1
n_check=1
num = 0

fb=[]

          
def init():
    global passc,index,fb
    fb=[]
    pass_init(0)
    index=1

def pass_init(noti_n):
    global PASS,level,fb,tmr,det,PASS_T,noti,n_check,btn
    level=0
    fb.clear()
    tmr=0
    det=[0,0,0]
    noti=noti_n
    n_check=1
    btn=-1
    
    for i in range(3):
        PASS[i][0]=random.randint(0,3)
        random.shuffle(PASS[i][1])
    for i in range(4):
        PASS_T[i]=random.randint(60,450)

    with open('flg/trouble/bar_pass.binary','wb') as web:
        pickle.dump(PASS_T,web)
        
    with open('flg/trouble/trouble.binary','wb') as web:
        pickle.dump(noti_n,web)

def next_level(fb_n,fb_p,noti_n):
    global level,fb,tmr,n_check,noti
    level+=1
    fb.append([fb_n,fb_p])
    tmr=0
    n_check=1
    noti=noti_n
    
    with open('flg/trouble/trouble.binary','wb') as web:
        pickle.dump(noti_n,web)

    
def draw(bg, fnt1, fnt2, fnt3, fnt4, fnt5):
    global check,date2,index
    
    bg.fill(BLACK)

    title1 = fnt3.render("Analyzed Structure", True, BLACK)
    title2 = fnt3.render("Progress", True, BLACK)
    title3 = fnt3.render("Genomic Analysis", True, BLACK)


    text1 = fnt5.render("Current State >", True, BLUE)
    text2 = fnt5.render("Achievement >", True, BLUE)

    STA = [fnt4.render("Not Achieved", True, RED),
            fnt4.render("Completed", True, GREEN)]

    Prog_c = [fnt1.render("Operation 1", True, BLACK),
              fnt1.render("Operation 2", True, BLACK),
              fnt1.render("Operation 3", True, BLACK),
              fnt1.render("Operation 3", True, BLACK)]

    
    Prog = [fnt4.render("Operation 1 : ", True, BLACK),
            fnt4.render("Operation 2 : ", True, BLACK),
            fnt4.render("Operation 3 : ", True, BLACK)]

    TEXT = [fnt2.render("SW1", True, BLACK),
            fnt2.render("SW2", True, BLACK),
            fnt2.render("SW3", True, BLACK),
            fnt2.render("SW4", True, BLACK)]


    bg.blit(BACK, (0,0))
        
    bg.blit(animation(DNA, 0.624, 0.556, 0), (3, 24))
    bg.blit(animation(DNA_CODE, 1, 1, 1, 90), (325, 23))
    bg.blit(animation(CHROMAT, 1, 1, 2), (325, 142))

    bg.blit(title1, (10, 7))
    bg.blit(title2, (10, 358))
    bg.blit(title3, (332, 7))

    bg.blit(text1, (10, 380))
    bg.blit(text2, (10, 465))
    bg.blit(Prog_c[level], (20, 405))

      
    for i in range(len(Prog)):           
        bg.blit(Prog[i], (20, 490 +30*i))

    for i in range(len(det)):           
        bg.blit(STA[det[i]], (165, 490 +30*i))


    for i in range(len(TEXT)):
        bg.blit(TEXT[i], (350, 290 +75*i))
            
    if level<=2:  
        if 0<=tmr_l and tmr_l<=30:          
            bg.blit(LAMP[PASS[level][0]], (930, int(17 +82.5*PASS[level][0])))


        for i in range(4):          
            bg.blit(BAR[i+1], (557, int(285 +75*PASS[level][1][i])))

    if btn>=0:
        surface_a=pygame.Surface((70,45))
        surface_a.fill(BLACK)
        surface_a.set_alpha(150)
        bg.blit(surface_a,[435,279+75*btn])


    for i in range(len(Index)):
        Index[i] += 1
        Index[i] %= Max_num[i]

    if n_check==1:
        bg.blit(NOTI[noti], (170, 120))

def file():
    global num

    if num != 0:
        if mouse_c == 1 :
                if 0<=x and x<=23:
                    if 0 <= y and y <= 36:
                        num = 0
    else:  
        for i in range(len(DRAWS)):       
            if mouse_c==1 :
                if 74+253*i<=x and x<=243+253*i:
                    if 197 <= y and y <= 380:
                        num = i +1

                        
def draw_result(bg, fnt5):
    text1 = fnt5.render("Sample A", True, BLACK)
    text2 = fnt5.render("Sample B", True, BLACK)
    text3 = fnt5.render("Sample C", True, BLACK)
    text4 = fnt5.render("Sample D", True, BLACK)
    texts = [text1, text2, text3, text4]
    
    bg.fill(BLACK)
   
    for i in range(len(DRAWS) +1):
        if num == i:
            
            if num == 0:
                bg.fill(BLACK)
                bg.blit(Back_file, (0, 0))
                for i in range(len(texts)):
                    bg.blit(texts[i], (94 +253*i, 390))
            else:
                bg.fill(WHITE)
                bg.blit(DRAWS[i-1][0], (30, 25))
                bg.blit(DRAWS[i-1][1], (330, 0))
                bg.blit(DRAWS[i-1][2], (630, 0))
                bg.blit(DRAWS[i-1][3], (630, 150))
                bg.blit(DRAWS[i-1][4], (630, 300))
                bg.blit(DRAWS[i-1][5], (630, 450))

                bg.blit(DRAWS_2[i-1], (200, 250))
            if 1 <= num:
                bg.blit(RET, (0, 0))


def game():
    global det,btn,n_check,index
    if tmr==1:
        btn=-1
        for i in range(level):
            det[i]=1
    if mouse_c==1 and tmr>=10:
        for i in range(4):
            if 760<=x and x<=790:
                if 125<=y and y<=160:
                    n_check=0
            if 435<=x and x<=500:
                if 280+75*i<=y and y<=325+75*i:
                    btn=i
                    if level==0:
                        if PASS[level][0]==0:
                            if i==1:
                                next_level(i,PASS[level][1].index(i),7)
                                index=2
                            else:
                                pass_init(4)
                        elif PASS[level][0]==1:
                            if i==1:
                                next_level(i,PASS[level][1].index(i),7)
                                index=2
                            else:
                                pass_init(4)
                        elif PASS[level][0]==2:
                            if i==2:
                                next_level(i,PASS[level][1].index(i),7)
                                index=2
                            else:
                                pass_init(4)
                        elif PASS[level][0]==3:
                            if i==3:
                                next_level(i,PASS[level][1].index(i),7)
                                index=2
                            else:
                                pass_init(4)
                                
                    elif level==1:
                        if PASS[level][0]==0:
                            if i==fb[0][0]:
                                next_level(i,PASS[level][1].index(i),2)
                            else:
                                pass_init(5)
                        elif PASS[level][0]==1:
                            if i==PASS[level][1][fb[0][1]]:
                                next_level(i,PASS[level][1].index(i),2)
                            else:
                                pass_init(5)
                        elif PASS[level][0]==2:
                            if i==0:
                                next_level(i,PASS[level][1].index(i),2)
                            else:
                                pass_init(5)
                        elif PASS[level][0]==3:
                            if i==PASS[level][1][fb[0][1]]:
                                next_level(i,PASS[level][1].index(i),2)
                            else:
                                pass_init(5)
                                
                    elif level==2:
                        if PASS[level][0]==0:
                            if i==PASS[level][1][fb[1][1]]:
                                next_level(i,PASS[level][1].index(i),3)
                            else:
                                pass_init(6)
                        elif PASS[level][0]==1:
                            if i==PASS[level][1][fb[0][1]]:
                                next_level(i,PASS[level][1].index(i),3)
                            else:
                                pass_init(6)
                        elif PASS[level][0]==2:
                            if i==fb[0][0]:
                                next_level(i,PASS[level][1].index(i),3)
                            else:
                                pass_init(6)
                        elif PASS[level][0]==3:
                            if i==fb[1][0]:
                                next_level(i,PASS[level][1].index(i),3)
                            else:
                                pass_init(6)
                                
    if level==3 and tmr>=100:
        index=3

def trouble_draw(bg):
    bg.fill(WHITE)
    bg.blit(BACK_T, (0,0))

    for i in range(len(color_bar)):
        pygame.draw.rect(bg, color_bar[i], (200 +185*i, y_bar[i], 66, 422-(y_bar[i] -45)))
    for i in range(4):  
        bg.blit(IND, [194 +185*i, y_bar[i] -15])
        
    if n_check==1:
        bg.blit(NOTI[noti], (170, 120))
                                
def trouble_game():
    global n_check,y_bar,index,n_check,noti,tmr
    
    if mouse_c==1:
        if 760<=x and x<=790:
            if 125<=y and y<=160:
                n_check=0
        for i in range(4):
            if 200+185*i<=x and x<=266+185*i:
                if 45<=y and y<=465:
                    y_bar[i]=y
                    tmr=0

    if tmr>=30:
        cnt=0
        for i in range(4):
            if PASS_T[i]-15<=y_bar[i] and y_bar[i]<=PASS_T[i]+15:
                cnt+=1
        
        if cnt==4:
            index=1
            noti=8
            n_check=1
            with open('flg/trouble/trouble.binary','wb') as web:
                pickle.dump(noti,web)
        tmr=0

    if tmr_l%5==0:
        with open('flg/trouble/bar.binary','wb') as web:
            pickle.dump(y_bar,web)
                    
            
            
def main():
    
    pygame.init()
    pygame.display.set_caption("PASS")
    screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
    
    clock = pygame.time.Clock()
    font1 = pygame.font.Font(None, 60)
    font2 = pygame.font.Font(None, 40)
    font3 = pygame.font.Font(None, 22)
    font4 = pygame.font.Font(None, 30)
    font5 = pygame.font.Font(None, 27)


    while True:
        global tmr,tmr_l,mouse_c,x,y,col,check,date2,tmr_i
    
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen=pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
                if event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((WIDTH,HEIGHT))
                if event.key == K_F12:
                    init()
                    
        key = pygame.key.get_pressed()
        x,y = pygame.mouse.get_pos()
        mouse_c,btn2,btn3 = pygame.mouse.get_pressed()
        tmr+=1
        tmr_l+=1
        tmr_l%=60
        tmr_i+=1
        tmr_i%=10
                
        if index == 0:
            init()
        if index == 1:
            draw(screen, font1, font2, font3, font4, font5)
            game()
        if index==2:
            trouble_draw(screen)
            trouble_game()
        if index==3:
            file()
            draw_result(screen, font5)
            ch=1
            with open('../../progress/flg/stage2.binary','wb') as web:
                try:
                    pickle.dump(ch,web)
                except:
                    pass
                
        check_i=0
        if tmr_i==0:
            with open('flg/init.binary','rb') as web:
                try:
                    check_i=pickle.load(web)
                except:
                    pass
        if check_i==1:
            ch=0
            with open('flg/init.binary','wb') as web:
                pickle.dump(ch,web)
            init()

        pygame.display.update()
        clock.tick(FPS)


if __name__=='__main__':
    main()
