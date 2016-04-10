# -*- coding:utf-8 -*-
import pygame, sys

n = 4 # размер матрицы (n*n)

window = pygame.display.set_mode((n*100+3, n*100+3), pygame.NOFRAME, 32) # создаем окно с размерами (количесво плиток * размеры плиток + небольшой отступ);
                                                                        #  pygame.NOFRAME - окно без границ, 32 - глубина цвета
pygame.display.set_caption('Крестики-нолики') # название окна (которое впринципе не нужно) =)
screen = pygame.Surface((n*100+3, n*100+3), pygame.SRCALPHA) # разрешаем использование альфа-канала (управление прозрачностью)

pygame.font.init() # инициализация шрифтов
FF = pygame.font.Font('DejaVuSans-ExtraLight.ttf', n*5) # маленький шрифт

class Button:
    def __init__(self, x = 0, y = 0, title = 'Button', width = 50, height = 30, title_color = (255, 255, 0, 255)):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = (100, 100, 100)
        self.surface = pygame.Surface((width, height))
        self.title = title
        self.click = False
        pygame.font.init()
        self.Button_font = pygame.font.Font('DejaVuSans-ExtraLight.ttf', int(self.height/1.5))
        self.title_color = title_color

    def active_button(self):
        mx, my = pygame.mouse.get_pos()
        if mx > self.x and mx < self.x+self.width and my > self.y and my < self.y+self.height:
            return True

    def render(self, screen):
        if self.active_button() == True:
            self.surface.fill((self.color[0]+10, self.color[1]+10, self.color[2]+10))
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.click = True
        else:
            self.surface.fill(self.color)
            self.click = False
        pygame.draw.aaline(self.surface,
                           (self.color[0]+100, self.color[1]+100, self.color[2]+100),
                           (1, 1),
                           (self.width-2, 1), 1)
        pygame.draw.aaline(self.surface,
                           (self.color[0]+100, self.color[1]+100, self.color[2]+100),
                           (1, 1),
                           (1, self.height-2), 1)
        pygame.draw.aaline(self.surface,
                           (self.color[0]-30, self.color[1]-30, self.color[2]-30),
                           (self.width-2, 3),
                           (self.width-2, self.height-2), 1)
        pygame.draw.aaline(self.surface,
                           (self.color[0]-30, self.color[1]-30, self.color[2]-30),
                           (2, self.height-2),
                           (self.width-2, self.height-2), 1)
        posx_title = (self.width-(self.height/3 * len(self.title)))/2
        self.surface.blit(self.Button_font.render(self.title, 1, (255,255,0,255)), (posx_title, 2))
        screen.blit(self.surface, (self.x, self.y))

class Plitka: # класс для создания плиток (квадратов) на которых и будут ставиться метки (крестики и нолики)
    def __init__(self, size, clr, x, y, value = 0): # передаваемые параметры - размер (должен быть кортеж), цвет, x и у начальные координаты, метка
        self.size = size # размер
        self.plitka = pygame.Surface((self.size)) # собственно сама плитка
        self.color = pygame.color.Color(clr[0], clr[1], clr[2]).hsva # цвет плитки по HSVA цветовой модели
        self.plitka.fill((self.color)) # закраска плитки
        self.value = value # метка
        self.x = x # икс координата
        self.y = y # игрек координата

    def render(self, surface): # функция отрисовки плитки
        self.plitka.fill(self.color) # закраска плитки
        if self.value == 1: # если плитка помечена единицей (первый игрок), то рисуем круг (нолик)
            pygame.draw.circle(self.plitka, (120, 200, 0), (int(self.size[0]/2),int(self.size[0]/2)), int(self.size[0]/2)-5, 1)
            self.plitka.blit(FF.render('1', 1, (120, 200, 0)), (self.size[0]/2, self.size[0]/2))
        elif self.value == 2: # иначе если плитка помечена двойкой (второй игрок), то рисуем крестик
            pygame.draw.line(self.plitka, (0, 180, 180), (int(self.size[0]/10), int(self.size[0]/10)), (int(self.size[0]-int(self.size[0]/10)), int(self.size[0]-int(self.size[0]/10))), 1)
            pygame.draw.line(self.plitka, (0, 180, 180), (int(self.size[0]/10), int(self.size[0]-int(self.size[0]/10))), (int(self.size[0]-int(self.size[0]/10)), int(self.size[0]/10)), 1)
            self.plitka.blit(FF.render('2', 1, (0, 180, 180)), (self.size[0]/2, self.size[0]/2))
        surface.blit(self.plitka, (self.x, self.y)) # отображаем покрашеную и украшеную плитку на игровой экран

def gen_matrix(n): # функция генерации матрицы с чистыми плитками
    matrix = []
    y = 2
    for i in range(n):
        a = []
        x = 2
        for j in range(n):
            a.append(Plitka((99, 99), (170, 170, 170), x, y, 0))
            x += 100
        matrix.append(a)
        y += 100
    return matrix

def game(matrix):
    # переключатели ходов
    player1 = True
    player2 = False

    # список содержит начало и конец линии (линия для показа победной цепочки), а так же номер победителя
    winner = [(''), (''), 0]

    # определяем какой длины нужно выстроить цепочку игроку для победы
    if len(matrix) < 5:
        first_player_control = '1'*len(matrix)
        second_player_control = '2'*len(matrix)
    else:
        first_player_control = '1'*5
        second_player_control = '2'*5

    # игровой цикл
    done = True
    pygame.mouse.set_pos((int(screen.get_width()/2), int(screen.get_width()/2)))
    while done:

        # управление
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    done = False

        # закраска экрана
        screen.fill((150, 100, 80))

        # если номер победителя = 0 (победитель не определен), то производим поиск цепочек, а так же отслеживаем действия игроков
        if winner[2] == 0:
            mx, my = pygame.mouse.get_pos() # берем координаты курсора мыши
            for i in matrix: # берем строку из матрицы
                for j in i: # берем элемент строки (квадрат)
                    if mx > j.x and my > j.y and mx < j.x + j.size[0] and my < j.y + j.size[1]: # сверяем координаты элемента и курсора мыши
                        if pygame.mouse.get_pressed() == (1, 0, 0): # если нажата левая кнопка мыши
                            if player1 == True: # если первый игрок имеет право ходить
                                if j.value == 0: # если данный квадрат не помечен
                                    j.value = 1 # метим его единицей
                                    player1 = False # запрещаем ходить первому игроку
                                    player2 = True # разрешаем ходить второму игроку
                            elif player2 == True:  #
                                if j.value == 0:   #
                                    j.value = 2    #тут все аналогично, но для второго игрока
                                    player1 = True #
                                    player2 = False#
                    j.render(screen) # отрисовываем обработанный квадрат на игровом экране

            # поиск победной цепочки по диагонали
            cont_list = ''
            for i in range(len(matrix)):
                cont_list += str(matrix[i][i].value)
            if first_player_control in cont_list:
                winner = ((5, 5), (screen.get_width()-5, screen.get_width()-5), 1)
            elif second_player_control in cont_list:
                winner = ((5, 5), (screen.get_width()-5, screen.get_width()-5), 2)

            # поиск победной цепочки по обратной диагонали
            cont_list = ''
            for i in range(len(matrix)):
                n = len(matrix)-1
                cont_list += str(matrix[i][n - i].value)
            if first_player_control in cont_list:
                winner = ((screen.get_width()-5, 5), (5, screen.get_width()-5), 1)
            elif second_player_control in cont_list:
                winner = ((screen.get_width()-5, 5), (5, screen.get_width()-5), 2)

            # поиск победной цепочки по горизонтали (строкам матрицы)
            for i in range(len(matrix)):
                cont_list = ''
                for j in range(len(matrix)):
                    cont_list += str(matrix[i][j].value)
                if first_player_control in cont_list:
                    winner = ((5, matrix[0][0].size[0]*i + matrix[0][0].size[0]/2), (screen.get_width()-5, matrix[0][0].size[0]*i + matrix[0][0].size[0]/2), 1)
                    continue
                elif second_player_control in cont_list:
                    winner = ((5, matrix[0][0].size[0]*i + matrix[0][0].size[0]/2), (screen.get_width()-5, matrix[0][0].size[0]*i + matrix[0][0].size[0]/2), 2)
                    continue

            # поиск победной цепочки по вертикали (столбцам матрицы)
            for i in range(len(matrix)):
                cont_list = ''
                for j in range(len(matrix)):
                    cont_list += str(matrix[j][i].value)
                if first_player_control in cont_list:
                    winner = ((matrix[0][0].size[0]*i + matrix[0][0].size[0]/2, 5), (matrix[0][0].size[0]*i + matrix[0][0].size[0]/2, screen.get_width()-5), 1)
                    continue
                elif second_player_control in cont_list:
                    winner = ((matrix[0][0].size[0]*i + matrix[0][0].size[0]/2, 5), (matrix[0][0].size[0]*i + matrix[0][0].size[0]/2, screen.get_width()-5), 2)
                    continue

        else: # если номер победителя не равен нулю (winner[2] != 0)
            screen.fill((50, 50, 50, 10)) # то закрашиваем экран
            pygame.draw.line(screen, (180, 0, 0), winner[0], winner[1], 10) # рисуем линию пересекающую победную цепочку
            screen.blit(FF.render(u"Выиграл "+str(winner[2])+u" игрок.", 1, (255, 255, 0, 50)), (screen.get_width()/4, screen.get_height()/2)) # Пишем сообщение о том кто выиграл
            screen.blit(FF.render(u"Esc - в меню", 1, (150, 150, 150, 50)), (5, 5)) # Пишем сообщение о том кто выиграл

        window.blit(screen, (0, 0)) # отображаем все на игровой экран
        pygame.display.flip() # отображаем все в окне
    return winner[2] # когда кто-то выиграет, игровой цикл завершится и после его завершения функция game возвратит значение winner[2] обозначающее номер победителя

# тут мы начинаем главный цикл, в котором реализовано очень простое меню
done = True
pygame.key.set_repeat(1000, 0) # а это секундная задержка между нажатиями клавиш (если её не будет,
                               # то мгновенное нажатие клавиши ESC во время игры сработает не только в игре но и в меню, что приведет к выходу из программы)
bt_start = Button(100, 145, 'Start',220, 40)
bt_quit = Button(100, 190, 'Quit',220, 40)
while done:
    # управление
    for e in pygame.event.get():
        pass

    if bt_start.click == True:
        bt_start.click = False
        winner = game(gen_matrix(n))
    if bt_quit.click == True:
        done = False

    # что написано ниже, думаю, всем понятно =)
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (125, 10, 10), (0, 0, screen.get_width(), screen.get_width()/3), 0)
    pygame.draw.rect(screen, (125, 10, 10), (0, screen.get_width()/1.6, n*100+3, screen.get_width()/2.5), 0)
    bt_start.render(screen)
    bt_quit.render(screen)
    window.blit(screen, (0, 0))
    pygame.display.flip()