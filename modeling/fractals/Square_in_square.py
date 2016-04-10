# -*- coding:utf-8 -*-

import pygame

W, H = 1600, 900
N = 55
DT = 15
SD = 0

window = pygame.display.set_mode((W, H), pygame.FULLSCREEN)
screen = pygame.Surface((W, H))

pnt = [[SD, SD], [W-SD, SD], [W-SD, H-SD], [SD, H-SD]]

done = True
b = 0
iD = 0
IC = 0
clock = pygame.time.Clock()
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                done = False

    screen.fill((0, 0, 0))

    d = iD
    b = IC

    x, y = 0, 0
    sp = [[SD, SD], [W-SD, SD], [W-SD, H-SD], [SD, H-SD]]
    for i in range(N):
        b += d * 5
        if b >= 255:
            d = -1
        if b <= 0:
            d = 1
        pygame.draw.polygon(screen, (b, 0, b), sp, 0)
        mx = sp[0][0]
        my = sp[0][1]
        sp[0][0] += (sp[1][0] - sp[0][0])//DT
        sp[0][1] += (sp[1][1] - sp[0][1])//DT

        sp[1][0] += (sp[2][0] - sp[1][0])//DT
        sp[1][1] += (sp[2][1] - sp[1][1])//DT

        sp[2][0] += (sp[3][0] - sp[2][0])//DT
        sp[2][1] += (sp[3][1] - sp[2][1])//DT

        sp[3][0] += (mx - sp[3][0])//DT
        sp[3][1] += (my - sp[3][1])//DT

    if IC >= 255:
        iD = 1
    if IC <= 0:
        iD = -1
    IC -= iD * 5

    window.blit(screen, (0, 0))
    pygame.display.flip()
    clock.tick(25)