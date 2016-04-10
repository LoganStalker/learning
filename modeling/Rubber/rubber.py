# -*- coding: utf-8 -*-
import pygame
from math import sqrt

window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400,400))

class tochka():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

def former(n):
    thk = []
    for i in range(n):
        t = tochka(200+i*200/n, i*10/n)
        thk.append(t)
    return thk

def play_rubber(speed, Toughness, Stiffness, zvenja, Weight):
    window = pygame.display.set_mode((400, 400))
    screen = pygame.Surface((400,400))
    pygame.init()
    DELTA_T = 100000.0
    t =       10000000.0
    p = former(zvenja)
    done = True
    while done:
        screen.fill((0,0,0))
    
        for i in range(1,len(p)):
            ax = 0
            ay = 0
            a = 0
            p0 = p[i-1]
            p1 = p[i]
        
            d = sqrt((p1.x-p0.x)**2+(p1.y-p0.y)**2)
            rest = 180.0/(len(p))
            if d > rest:
                a = Stiffness*(d-rest)
            if d < 2:
                a = 1E-0*(2-d)
        
            ax = a*(p0.x-p1.x)/d
            ay = a*(p0.y-p1.y)/d
            p1.vx += ax*DELTA_T/t
            p1.vy += ay*DELTA_T/t
            if i != 1:
                p0.vx -= ax*DELTA_T/10000000.0
                p0.vy -= ay*DELTA_T/10000000.0
            
        p[len(p)-1].vy += (1E-1)*Weight
        for i in p:
            i.vx *= 1-2*10**(Toughness*(-1))
            i.vy *= 1-2*10**(Toughness*(-1))
            i.x += i.vx*DELTA_T/t*speed
            i.y += i.vy*DELTA_T/t*speed

        for i in range(1,len(p)):
            pygame.draw.line(screen, (0, 255, 0), (p[i-1].x,p[i-1].y), (p[i].x,p[i].y), 1)
            pygame.draw.circle(screen, (255, 0, 0), (int(p[i].x), int(p[i].y)), 2, 0)
            if i==len(p)-1:
                pygame.draw.circle(screen, (0,255,0), (int(p[i].x),int(p[i].y)+5), 5, 0)
    
        window.blit(screen,(0,0))
        pygame.display.flip()
                
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.display.quit()
                done = False