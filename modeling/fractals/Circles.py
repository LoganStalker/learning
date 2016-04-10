# -*- coding:utf-8 -*-

import pygame
from math import sin, cos

SIZE = (800, 800)
DEPTH = 4
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Фрактал')

screen = pygame.Surface(SIZE)

class fract_circle:
    def __init__(self, x, y, radius, color, by = 0, plus=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.plus = plus
        self.by = by
        self.bitmap = pygame.Surface(((self.radius+1)*2, (self.radius+1)*2))
        self.bitmap.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.bitmap, self.color, (int(self.radius+1), int(self.radius+1)), int(self.radius), 1)

    def render(self, surface):
        surface.blit(self.bitmap, (self.x, self.y))

    def redraw(self):
        self.bitmap.fill((0, 0, 0))
        pygame.draw.circle(self.bitmap, self.color, (int(self.radius+1), int(self.radius+1)), int(self.radius), 1)

def gen_fract(depth):
    circles = list()
    r = SIZE[0]/2
    for i in range(depth+1):
        circle = fract_circle(0, 0, r, (200, 200, 0))
        r /= 3
        if r < 1:
            r = 1
        circles.append(circle)
    return circles

circles = gen_fract(DEPTH)

def draw_fract(circles, n=0):
    for i in range(6):
        circles[n].plus+=1.05
        circles[n].by-=0.0001+((n-1))*0.004975
        circles[n].x = circles[n-1].radius/1.49 + sin(circles[n].by - circles[n].plus) * circles[n-1].radius/1.5
        circles[n].y = circles[n-1].radius/1.49 + cos(circles[n].by - circles[n].plus) * circles[n-1].radius/1.5
        circles[n].render(circles[n-1].bitmap)
        pygame.draw.line(circles[n-1].bitmap, (0, 200, 200), (int(circles[n-1].bitmap.get_width()/2), int(circles[n-1].bitmap.get_height()/2)),
                         (circles[n].x + int(circles[n].bitmap.get_height()/2), circles[n].y + int(circles[n].bitmap.get_width()/2)), 1)

        if circles[n].by < -36:
            circles[n].by = 0
            circles[n].plus = 0

    circles[n-1].bitmap.blit(circles[n].bitmap, (circles[n-1].bitmap.get_width()/2.99, circles[n-1].bitmap.get_height()/2.99))

    n -= 1
    if n != 0:
        draw_fract(circles, n)

    return circles[0]

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False

    screen.fill((110, 40, 40))

    for c in circles:
        c.redraw()

    m = draw_fract(circles, len(circles)-1)

    m.render(screen)

    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
