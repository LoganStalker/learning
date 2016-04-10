# -*- coding:utf-8 -*-
import pygame
import math

siz=800
window=pygame.display.set_mode((siz,siz))
pygame.init()

def make_structure(size):
    glubina=3 # это глубина фрактала(Если это можно назвать фракталом)
    laps=[]
    radiuses=[]
    radius=size/2.5
    radiuses.append(radius)
    sizes=size
    for i in range(glubina+1):
        lap = pygame.Surface((sizes,sizes))
        pygame.draw.circle(lap, (0, 0, 0), (int(size/2), int(size/2)), int(size/2), 0)
        laps.append(lap)
        sizes/=5
        if sizes<1:
            sizes=1
    for i in range(glubina):
        radius/=5
        radiuses.append(radius)
    by=[0]*(glubina)
    plus=[0]*(glubina)
    if sizes!=0:
        sizes*=5
    return laps, radiuses, by, plus, sizes

def draw_structure(laps, radiuses, n, by, plus, speed):
    for i in range(9):
        plus[n-1]+=0.7
        by[n-1]-=0.001+((n-1)*speed)
        laps[n-1].blit(laps[n],(radiuses[n-1]+math.sin(by[n-1]-plus[n-1])*radiuses[n-1],
                                radiuses[n-1]+math.cos(by[n-1]-plus[n-1])*radiuses[n-1]))
    plus[n-1]=0
    if by[n-1]<-360:
        by[n-1]=0
    n-=1
    if n!=0:
        draw_structure(laps,radiuses,n,by,plus, 0.01)
    return laps[0], by

struc=[]
cn=1
for i in range(7):
    print(cn)
    struc.append(make_structure(siz/cn))
    cn+=0.04
    
ccol=[[0,1,2],
      [2,0,1],
      [1,2,0],
      [2,1,0],
      [0,2,1],
      [1,0,2],
      [2,1,2],]
done=True
d=0  #это задержка - delay
colors=[0,0,0]
filka=True
speed = 0.01
while done:
    n=len(struc[0][0])-1
    
    if colors[0]!=255 and colors[1]==0 and colors[2]==0:
        colors[0]+=1
    if colors[0]==255 and colors[1]!=255 and colors[2]==0:
        colors[1]+=1
    if colors[1]==255 and colors[2]==0 and colors[0]!=0:
        colors[0]-=1
    if colors[0]==0 and colors[1]==255 and colors[2]!=255:
        colors[2]+=1
    if colors[0]==0 and colors[1]!=0 and colors[2]==255:
        colors[1]-=1
    if colors[0]!=255 and colors[1]==0 and colors[2]==255:
        colors[0]+=1
    if colors[0]==255 and colors[1]!=255 and colors[2]==255:
        colors[1]+=1
    if colors[0]==255 and colors[1]==255 and colors[2]==255:
        colors[0]=0
        colors[1]=0
        colors[2]=0
    
    for j in range(len(struc)):
        for i in range(n+1):
            if i==n:
                struc[j][0][i].fill((colors[ccol[j][0]],colors[ccol[j][1]],colors[ccol[j][2]]))
            else:
                struc[j][0][i].fill((0,0,50))
                struc[j][0][i].set_colorkey((0,0,50))
    m=[]
    for i in range(len(struc)):
        m.append(draw_structure(struc[i][0],struc[i][1],n,struc[i][2],struc[i][3], speed))
    
    if filka==True:
        window.fill((50,50,50))
    window.blit(m[6][0],(76,76))
    window.blit(m[5][0],(66,66))
    window.blit(m[4][0],(55,55))
    window.blit(m[3][0],(43,43))
    window.blit(m[2][0],(30,30))
    window.blit(m[1][0],(15,15))
    window.blit(m[0][0],(0,0))
    window.blit(pygame.font.Font(None,28).render(u"Задержка: ", 1, (250,250,0)), (0,0))
    window.blit(pygame.font.Font(None,28).render(str(d), 1, (250,250,0)), (120,0))
    pygame.display.flip()
    pygame.time.delay(d)

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_SPACE:
                pygame.image.save(window, '2.jpg')
            if e.key==pygame.K_DOWN:
                d-=10
                if d<0:
                    d=0
            if e.key==pygame.K_UP:
                d+=10
                if d>50:
                    d=50
            if e.key==pygame.K_f:
                if filka==True:
                    filka=False
                else:
                    filka=True
            if e.key==pygame.K_ESCAPE:
                done=False
            if e.key == pygame.K_s:
                speed += 0.001
            if e.key == pygame.K_x:
                speed -= 0.001
            if e.key==pygame.K_UP:
                d+=10
                if d>50:
                    d=50