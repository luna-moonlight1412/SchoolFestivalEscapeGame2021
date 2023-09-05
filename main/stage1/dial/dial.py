import pygame
import sys
from pygame.locals import*
import random
import pickle

sys.path.append('../../')
from crackingscreen import crackingscreen

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
YELLOW=(255,255,0)

COLOR=[(255,255,255),(255,0,0)]



ALPHABET=[pygame.image.load("image/alphabet/a.png"),
          pygame.image.load("image/alphabet/b.png"),
          pygame.image.load("image/alphabet/c.png"),
          pygame.image.load("image/alphabet/d.png"),
          pygame.image.load("image/alphabet/e.png"),
          pygame.image.load("image/alphabet/f.png"),
          pygame.image.load("image/alphabet/g.png"),
          pygame.image.load("image/alphabet/h.png"),
          pygame.image.load("image/alphabet/i.png"),
          pygame.image.load("image/alphabet/j.png"),
          pygame.image.load("image/alphabet/k.png"),
          pygame.image.load("image/alphabet/l.png"),
          pygame.image.load("image/alphabet/m.png"),
          pygame.image.load("image/alphabet/n.png"),
          pygame.image.load("image/alphabet/o.png"),
          pygame.image.load("image/alphabet/p.png"),
          pygame.image.load("image/alphabet/q.png"),
          pygame.image.load("image/alphabet/r.png"),
          pygame.image.load("image/alphabet/s.png"),
          pygame.image.load("image/alphabet/t.png"),
          pygame.image.load("image/alphabet/u.png"),
          pygame.image.load("image/alphabet/v.png"),
          pygame.image.load("image/alphabet/w.png"),
          pygame.image.load("image/alphabet/x.png"),
          pygame.image.load("image/alphabet/y.png"),
          pygame.image.load("image/alphabet/z.png")]


CODE=[[['a','b','c','d','e'],
       ['g','e','f','h','i'],
       ['e','d','f','g','h'],
       ['n','m','o','p','q'],
       ['t','u','v','w','x']],


      [['a','b','c','d','e'],
       ['r','q','s','t','u'],
       ['c','a','b','d','e'],
       ['h','i','j','k','l'],
       ['e','c','d','f','g']],


      [['a','b','c','d','e'],
       ['v','s','t','u','w'],
       ['o','n','p','q','r'],
       ['i','j','k','l','m'],
       ['d','a','b','c','e']],


      [['a','b','c','d','e'],
       ['w','v','x','y','z'],
       ['a','b','c','d','e'],
       ['k','h','i','j','l'],
       ['e','a','b','c','d']],


      [['b','a','c','d','e'],
       ['l','k','m','n','o'],
       ['e','f','g','h','i'],
       ['s','t','u','v','w'],
       ['s','o','p','q','r']],


      [['b','a','c','d','e'],
       ['l','k','m','n','o'],
       ['o','p','q','r','s'],
       ['c','a','b','d','e'],
       ['k','h','i','j','l']],


      [['b','a','c','d','e'],
       ['l','j','k','m','n'],
       ['o','p','q','r','s'],
       ['o','k','l','m','n'],
       ['d','a','b','c','e']],


      [['b','a','c','d','e'],
       ['r','q','s','t','u'],
       ['e','a','b','c','d'],
       ['a','b','c','d','e'],
       ['k','j','l','m','n']],


      [['c','a','b','d','e'],
       ['h','i','j','k','l'],
       ['a','b','c','d','e'],
       ['o','n','p','q','r'],
       ['s','t','u','v','w']],


      [['c','a','b','d','e'],
       ['r','q','s','t','u'],
       ['a','b','c','d','e'],
       ['m','l','n','o','p'],
       ['p','o','q','r','s']],


      [['c','a','b','d','e'],
       ['r','n','o','p','q'],
       ['i','g','h','j','k'],
       ['m','i','j','k','l'],
       ['e','a','b','c','d']],


      [['c','a','b','d','e'],
       ['r','o','p','q','s'],
       ['o','k','l','m','n'],
       ['w','v','x','y','z'],
       ['n','o','p','q','r']],


      [['c','a','b','d','e'],
       ['o','k','l','m','n'],
       ['v','u','w','x','y'],
       ['i','j','k','l','m'],
       ['d','a','b','c','e']],


      [['d','a','b','c','e'],
       ['e','f','g','h','i'],
       ['a','b','c','d','e'],
       ['t','s','u','v','w'],
       ['h','i','j','k','l']],


      [['d','a','b','c','e'],
       ['i','f','g','h','j'],
       ['r','s','t','u','v'],
       ['t','q','r','s','u'],
       ['y','v','w','x','z']],


      [['e','a','b','c','d'],
       ['n','k','l','m','o'],
       ['e','a','b','c','d'],
       ['m','k','l','n','o'],
       ['y','v','w','x','z']],


      [['f','b','c','d','e'],
       ['a','b','c','d','e'],
       ['t','q','r','s','u'],
       ['a','b','c','d','e'],
       ['l','j','k','m','n']],


      [['f','b','c','d','e'],
       ['a','b','c','d','e'],
       ['t','q','r','s','u'],
       ['u','v','w','x','y'],
       ['m','i','j','k','l']],


      [['f','b','c','d','e'],
       ['a','b','c','d','e'],
       ['u','v','w','x','y'],
       ['l','h','i','j','k'],
       ['t','u','v','w','x']],


      [['f','b','c','d','e'],
       ['e','a','b','c','d'],
       ['v','w','x','y','z'],
       ['e','a','b','c','d'],
       ['r','q','s','t','u']],


      [['f','b','c','d','e'],
       ['i','f','g','h','j'],
       ['g','f','h','i','j'],
       ['h','i','j','k','l'],
       ['t','p','q','r','s']],


      [['p','l','m','n','o'],
       ['e','a','b','c','d'],
       ['r','q','s','t','u'],
       ['i','g','h','j','k'],
       ['l','i','j','k','m']],


      [['p','l','m','o','q'],
       ['u','t','v','w','x'],
       ['r','q','s','t','u'],
       ['g','c','d','e','f'],
       ['e','a','b','c','d']],



      [['s','q','r','t','u'],
       ['i','g','h','j','k'],
       ['l','k','m','n','o'],
       ['l','k','m','n','o'],
       ['y','v','w','x','z']],


      [['s','t','u','v','w'],
       ['n','o','p','q','r'],
       ['e','a','b','c','d'],
       ['a','b','c','d','e'],
       ['k','g','h','i','j']],


      [['s','t','u','v','w'],
       ['p','l','m','n','o'],
       ['o','k','l','m','n'],
       ['i','f','g','h','j'],
       ['l','m','n','o','p']],


      [['u','v','w','x','y'],
       ['s','o','p','q','r'],
       ['u','q','r','s','t'],
       ['r','s','t','u','v'],
       ['p','l','m','n','o']],


      [['u','v','w','x','y'],
       ['n','k','l','m','o'],
       ['i','h','j','k','l'],
       ['t','u','v','w','x'],
       ['y','v','w','x','z']],


      [['v','w','x','y','z'],
       ['e','i','r','a','o'],
       ['n','r','a','u','v'],
       ['o','l','s','r','h'],
       ['m','s','y','p','r']],


      [['v','w','x','y','z'],
       ['i','j','k','l','m'],
       ['r','s','t','u','v'],
       ['u','s','t','v','w'],
       ['s','o','p','q','r']]
      ]

PASS=[]
for i in range(len(CODE)):
    PASS.append([CODE[i][0][0],CODE[i][1][0],CODE[i][2][0],CODE[i][3][0],CODE[i][4][0]],)

index=0
tmr=0
tmr_i=0
x=0
y=0
mouse_c=0
touch=0

color=0
s=[0,0,0,0,0]
r=random.randint(0,len(PASS)-1)

def init():
    global r,PASS,index
    r=random.randint(0,len(CODE)-1)
    for i in range(len(CODE[r])):
        random.shuffle(CODE[r][i])
    index=1

def draw(bg,fnt):
    global tmr
    bg.fill(COLOR[color])
    if color==1:
        rx=random.randint(-5,5)
        ry=random.randint(-5,5)
    else:
        rx=0
        ry=0
    for i in range(5):
        pygame.draw.circle(bg,BLACK,[i*200+110+rx,70+ry],30)
        pygame.draw.circle(bg,BLACK,[i*200+110+rx,400+ry],30)
        bg.blit(ALPHABET[ord(CODE[r][i][s[i]])-97],[i*200+35+rx,135+ry])
    pygame.draw.rect(bg,WHITE,[200+rx,470+ry,620,80])
    pygame.draw.rect(bg,BLACK,[200+rx,470+ry,620,80],5)
    sur=fnt.render("ENTER",True,BLACK)
    bg.blit(sur,[380+rx,475+ry])
    if touch==1:
        surface_a=pygame.Surface((620,80))
        surface_a.fill(BLACK)
        surface_a.set_alpha(150)
        bg.blit(surface_a,[200+rx,470+ry])

def check(bg):
    global s,tmr,index,color,touch
    if tmr>5:
        color=0
        touch=0
    if mouse_c==1 and tmr>5:
        for i in range(5):
            if 80+i*200<=x and x<=140+i*200:
                if 40<=y and y<=100:
                    s[i]+=1
                    tmr=0
                if 370<=y and y<=430:
                    s[i]-=1
                    tmr=0
        if 200<=x and x<=820:
            if 470<=y and y<=550:
                t=[]
                for i in range(len(s)):
                    t.append(CODE[r][i][s[i]])
                if PASS[r]==t:
                    index=2
                    tmr=0
                else:
                    tmr=-7
                    color=1
                    touch=1
    for i in range(5):
        if s[i]>4:
            s[i]=0
        if s[i]<0:
            s[i]=4
            
def main():
    pygame.init()
    pygame.display.set_caption("PASS")
    screen=pygame.display.set_mode((1020,580),pygame.FULLSCREEN)
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,120)

    while True:
        global tmr,mouse_c,x,y,index,tmr_i
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
        tmr_i%10

        if index==0:
            init()
        if index==1:
            draw(screen,font)
            check(screen)
        if index==2:
            index=0
            ch=1
            with open('../../progress/flg/stage1_2.binary','wb') as web:
                pickle.dump(ch,web)
            ch=4
            crackingscreen.main(ch)

        check_i=0
        if tmr_i==0:
            with open('../../crackingscreen/flg/init_dial.binary','rb') as web:
                try:
                    check_i=pickle.load(web)
                except:
                    pass
        if check_i==1:
            ch=0
            with open('../../crackingscreen/flg/init_dial.binary','wb') as web:
                pickle.dump(ch,web)
            init()

                    
        pygame.display.update()
        clock.tick(30)

if __name__=='__main__':
    main()
