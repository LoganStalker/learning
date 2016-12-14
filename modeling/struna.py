# -*- coding: utf-8 -*-
import pygame, math
import scipy.integrate as spint

window = pygame.display.set_mode((1200,500))
screen = pygame.Surface((1200,500))

def fi(x):
    return math.cos(0.001*(x*x))*100
def psi(x):
    return -2*0.001*x*math.sin(0.001*(x*x))

def points_comput(t):
    points = []
    for x in range(45):
        a = 10
        integr = spint.quad(psi, (x - a*t), (x + a*t))
        u = ((fi(x - a*t) + fi(x + a*t))/2) + (1/(2*a))*integr[0]
        points.append((x*28, u+250))
    return points

done = True
t = 0
while done:
    screen.fill((20, 20, 20))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False
    
    t += 0.01
    if t == 40:
        t = 0
    
    points = points_comput(t)
    pygame.draw.aalines(screen, (0, 255, 0), False, points, 1)
    window.blit(screen, (0, 0))
    pygame.display.flip()