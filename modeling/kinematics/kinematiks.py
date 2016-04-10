# -*- coding:utf-8 -*-

from pygame import Surface, display, font, event, QUIT, KEYDOWN, K_SPACE,\
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_z, K_x, K_r, time, key, draw
from math import sin, cos, sqrt

window = display.set_mode((640, 490))
display.set_caption('Кинематика')

screen = Surface((640, 490))


def first_point(l1, w, t):
    x1 = l1*cos(w*t)
    y1 = l1*sin(w*t)
    return (x1, y1)

def second_point(l1, l2, w, t):
    cos_fi = sqrt(1-((l1/l2)*sin(w*t))**2)
    x2 = l1*cos(w*t)+l2*cos_fi
    y2 = 0
    return (x2, y2)

font.init()
FF = font.Font("Purisa.otf", 14)
small_FF = font.Font("Purisa.otf", 10)

width_lines = 3
radius = 7
t = 0
w = 4
l1 = 100.0
l2 = 300.0
h = 200
v = 250
v_for_red_point = 250
h_for_red_point = 200
done = True
razgon = False
key.set_repeat(500, 10)
while done:
    for e in event.get():
        if e.type == QUIT:
            done = False
        if e.type == KEYDOWN:
            if e.key == K_UP:
                if l1 > radius*2-1:
                    l1 -= 1
            if e.key == K_DOWN:
                if l1 < 175:
                    l1 += 1
            if e.key == K_LEFT:
                if l2 > radius*2-1:
                    l2 -= 1
            if e.key == K_RIGHT:
                if l2 < 450:
                    l2 += 1
            if e.key == K_z:
                w -= 1
                time.delay(50)
            if e.key == K_x:
                w += 1
                time.delay(50)
            if e.key == K_r:
                if razgon == False:
                    t = 0
                    razgon = True
                else:
                    w = 4
                    razgon = False
            if e.key == K_SPACE:
                time.delay(1000)

    screen.fill((50, 50, 50))

    t += 0.01
    if t > 100:
        t = 0

    if razgon == True:
        if w < 3000:
            w = t

    try:
        draw.rect(screen, (100, 100, 100), (5, 100, 630, 360), 0)
        pos_first_point = first_point(l1, w, t)
        pos_second_point = second_point(l1, l2, w, t)
        x1 = pos_first_point[0]+h
        y1 = pos_first_point[1]+v
        x2 = pos_second_point[0]+h_for_red_point
        y2 = pos_second_point[1]+v_for_red_point
        draw.line(screen, (0, 255, 0), (int(x1), int(y1)), (h, v), width_lines)
        draw.line(screen, (255, 255, 0), (int(x1), int(y1)), (int(x2), v_for_red_point), width_lines)
        draw.circle(screen, (0,255,0), (int(x1), int(y1)), radius, 0)
        draw.circle(screen, (0,255,0), (h, v), radius, 0)
        draw.circle(screen, (255,0,0), (int(x2), v_for_red_point), radius, 0)
    except:
        screen.blit(FF.render('Error in mathematical calculations: change the value of the long arm.', 1, (255, 255, 50)), (10, screen.get_height()/2))
    # vyvod inf
    screen.blit(FF.render('green', 1, (0, 255, 0)), (5, 0))
    screen.blit(FF.render('x: ', 1, (255, 255, 0)), (60, 0))
    screen.blit(FF.render('%.8f' % pos_first_point[0], 1, (0, 255, 100)), (75, 0))
    screen.blit(FF.render(',y: ', 1, (255, 255, 0)), (180, 0))
    screen.blit(FF.render('%.8f' % pos_first_point[1], 1, (0, 255, 100)), (200, 0))
    ##############
    screen.blit(FF.render('red', 1, (255, 0, 0)), (5, 20))
    screen.blit(FF.render('x: ', 1, (255, 255, 0)), (60, 20))
    screen.blit(FF.render('%.8f' % pos_second_point[0], 1, (0, 255, 100)), (75, 20))
    screen.blit(FF.render(',y: ', 1, (255, 255, 0)), (180, 20))
    screen.blit(FF.render('%.8f' % pos_second_point[1], 1, (0, 255, 100)), (200, 20))
    ##############
    screen.blit(FF.render('the distance between points: ', 1, (255, 255, 255)), (5, 40))
    distance_between_points = sqrt((x2-x1)**2 + (v_for_red_point-y1)**2)
    screen.blit(FF.render(str(distance_between_points), 1, (150, 150, 255)), (250, 40))
    screen.blit(small_FF.render('sqrt((x2 - x1)^2 + (y2 - y1)^2)', 1, (255, 255, 255)), (5, 60))
    ##############
    screen.blit(small_FF.render('Press up or down for change green line.', 1, (255, 255, 50)), (5, screen.get_height()-30))
    screen.blit(small_FF.render('Press left or right for change yellow line.', 1, (255, 255, 50)), (5, screen.get_height()-15))
    screen.blit(small_FF.render('Press z or x for change speed animation.', 1, (255, 180, 0)), (325, screen.get_height()-30))
    screen.blit(small_FF.render('Press r for change mode of animation.', 1, (255, 180, 0)), (325, screen.get_height()-15))
    ##############
    screen.blit(small_FF.render('L1 (green line):', 1, (255, 180, 0)), (5, 80))
    screen.blit(small_FF.render(str(l1), 1, (255, 255, 255)), (95, 80))
    screen.blit(small_FF.render('L2 (yellow line):', 1, (255, 180, 0)), (125, 80))
    screen.blit(small_FF.render(str(l2), 1, (255, 255, 255)), (220, 80))
    screen.blit(FF.render('Animation speed:', 1, (255, 180, 0)), (470, 5))
    screen.blit(FF.render(str(w), 1, (255, 255, 255)), (610, 5))

    window.blit(screen, (0, 0))
    display.update()