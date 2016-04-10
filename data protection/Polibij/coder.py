# -*- coding:utf-8 -*-

from pygame.sprite import Group
from pygame.display import set_mode, flip
from pygame.image import load
from pygame.transform import scale
from pygame import Surface, font, Color, event, K_ESCAPE, QUIT, KEYDOWN, MOUSEBUTTONUP
from Buttons import Button

SIZE = (600, 350)
PL_W = 30
PL_H = 30
BG_IMG = load('bg.png')
BACKGROUND = scale(BG_IMG, SIZE)
ALFAVIT = ('А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К',
           'Л','М','Н','О','П','Р','С','Т','У','Ф',
           'Х','Ц','Ч','Щ','Ш','Ъ','Ы','Ь','Э','Ю','Я','_',',','.')

window = set_mode(SIZE)
screen = Surface(SIZE)

font.init() # инициализация шрифтов обязательна, иначе модуль font не будет работать
ff = font.Font('fonts/Segoe Print Regular.ttf', 23)

Alfavit = Group()   # группа алфавита
message_group = Group() # группа кнопок сообщения
message_list = [] # данный список нужен для передачи сообщения в дешифрующую функцию
encode_message_group = Group()  # группа кнопок зашифрованного сообщения
button_group = Group()  # группа кнопок управления
decode_message = Group()    # группа кнопок дешифрованного сообщения

# добавляем кнопки с помощью модуля Button
pl = Button(x=300, y=30, width=175, height=35, text='Зашифровать', text_size=32, color=Color("#bf3030"))
button_group.add(pl)
pl = Button(300, 70, 175, 35, 'Дешифровать', 32, Color("#bf3030"))
button_group.add(pl)
pl = Button(300, 110, 175, 35, 'Стереть', 32, Color("#bf3030"))
button_group.add(pl)
pl = Button(300, 150, 175, 35, 'Показать коды', 32, Color("#bf3030"), alt_text='Показать текст')
button_group.add(pl)

x, y = 35, 30
col, row = 1, 1
# в цикле ниже создаем алфавитную таблицу
for i in ALFAVIT:   # перебираем символы алфавита
    pl = Button(x=x, y=y, width=PL_W, height=PL_H, text=i, color=(Color('#300571')))  # создаем новую кнопку
    pl.col = col    # задаем кнопке новое свойство col - это номер столбца в котором будет расположена кнопка
    pl.row = row    # задаем кнопке новое свойство row - это номер строки в которой будет расположена кнопка
    pl.font = font.Font('fonts/DS Crystal Regular.ttf', 21)    # задаем шрифт которым будет отображаться надпись на кнопке
    Alfavit.add(pl) # добавляем новую кнопку в группу Alfavit
    x += PL_W   # увеличиваем координату X на ширину кнопки, чтобы следующая кнопка отобразилась правее предыдущей
    col += 1    # увеличиваем номер столбца, так как следующая кнопка будет расположена в следующем столбце
    if x > 35+PL_W*5:   # если х координата больше расчетного значения для 6 столбца
        x = 35  # то отодгаем икс координату в начальное положение
        y += PL_H   # увеличиваем Y-координату, чтобы следующие объекты отображались на новой строке ниже
        row += 1    # увеличиваем значение строки
        col = 1 # значение столбца сбрасываем на начало отсчета

def encode(): # процедура шифрования
    mc = [] # список для номеров строк
    mc2 = []    # спискок для номеров столбцов
    for mess in message_list:   # перебираем символы из сообщения
        mc.append(mess.row)     # добавляем в список для номеров строк номер строки символа
        mc2.append(mess.col)    # добавляем в список для номеров столбцов номер столбца символ
    mc += mc2   # склеиваем списки - сначала номера строк, потом номера столбцов

    rez_message = []    # список для результирующего сообщения
    simbx = 150 # начальная позиция по Х для вывода сообщения
    for i in range(1, len(mc), 2):  # в данном цикле перебираем попарно символы из mc начиная с первого.
        for simb in Alfavit:    # перебираем символы алфавита
            if simb.col == mc[i]:   # если номер столбца совпадает со вторым числом из пары (перебираем попарно списком mc)
                if simb.row == mc[i-1]: # если номер строки совпадает с первым числом из пары
                    pl = Button(simbx, 260, PL_W, PL_H, simb.text)  # то создаем кнопку с текстом нажатой кнопки из алфавита
                    pl.col = simb.col   #   новой кнопке назначаем свойства col и row и передаем
                    pl.row = simb.row   # соответствующие значения от нажатой кнопки из алфавита
                    pl.font = simb.font
                    encode_message_group.add(pl) # добавляем новую кнопку в группу зашифрованного сообщения
                    rez_message.append(pl)  # так же помещаем кнопку в список зашифрованного сообщения
                    simbx += PL_W   # прибавляем к simbx значение ширины кнопки алфавита, чтобы сдвинуть следующую кнопку в право
    return rez_message  # передаем результат в виде списка

# по идее можно было обойтись без списка и перебирать объекты из группы зашифрованного сообщения, но они перебираются не по порядку, что делает дешифрование невозможным
def decode(message): # дешифратор
    m = []
    # в данном цикле формируем числовое представление сообщения для дальнейшей дешифровки
    for mess in message: # перебираем объекты из сообщения
        m.append(mess.row)  # добавляем в список m номер строки объекта из сообщения
        m.append(mess.col)  # добавляем в список m номер столбца объекта из сообщения

    # делим список пополам
    mc = m[0:(len(m)//2)]   #   первая часть списка это номера строк зашифрованного сообщения
    mc2 = m[(len(m)//2):(len(m))]   # вторая часть списка это номера столбцов зашифрованного сообщения

    simbx = 150 # переменная задающая х-координату формируемым объектам, дабы они отображались друг за дружкой, а не друг на друге
    for i in range(len(mc)):    # так как длины mc и mc2 одинаковы, то в цикле проходим от 0 до длины mc
        for simb in Alfavit:    # перебираем символы из алфавита
            if simb.col == mc2[i]:  # если номер столбца символа равен i-му числу из списка номеров столбцов
                if simb.row == mc[i]:   # если номер строки символа равен i-му числу из списка номеров строк
                    pl = Button(simbx, 290, PL_W, PL_H, simb.text)  # то создаем новую кнопку с текстом символа из алфавита
                    pl.row = simb.row   # задаем свойство row новому сиволу и присваиваем ему номер строки символа из алфавита
                    pl.col = simb.col   # задаем свойство col новому сиволу и присваиваем ему номер столбца символа из алфавита
                    pl.font = simb.font
                    decode_message.add(pl)  # добавляем новую кнопку в группу дешифрованного сообщения
                    simbx += PL_W   # прибавляем к simbx значение ширины кнопки алфавита, чтобы сдвинуть следующую кнопку в право

def show_codes(list_lists):
    '''
    в данной процедуре основной текст кнопки помещается свойству alt_text,
    а свойству text назначаются строковые значения номеров строки и столбца
    нужно для того чтобы показать коды сообщений - шифруемого и зашифрованного
    '''
    for l in list_lists:
        for button in l:
            button.alt_text = button.text
            button.text = str(button.row)+' '+str(button.col)
            button.font = font.Font('fonts/DS Crystal Regular.ttf', 16)

def show_text(list_lists):
    '''
    в данной процедуре основной текст кнопки заменяется её альтернативным текстом
    '''
    for l in list_lists:
        for button in l:
            button.text = button.alt_text
            button.font = font.Font('fonts/DS Crystal Regular.ttf', 21)

done = True
messx = 150
while done:
    mouse_click = False # данная переменная нужна для передачи события клика мышью
    for e in event.get():
        if e.type == QUIT:
            done = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                done = False
        if e.type == MOUSEBUTTONUP:
            mouse_click = True

    #screen.fill((60, 60, 54))
    screen.blit(BACKGROUND, (0,0))

    # тут набирается сообщение для шифрования/дешифрования
    for i in Alfavit:   # перебираем объекты группы алфавита
        i.update()  # вызывем для каждого объекта метод update
        if i.onClick(mouse_click):  # если по данной кнопке было произведено нажатие
            # создаем новую кнопку с номерами строки и столбца нажатого объекта, а так же с тем же шрифтом
            pl = Button(messx, 230, PL_W, PL_H, i.text)
            pl.col = i.col
            pl.row = i.row
            pl.font = i.font
            message_group.add(pl) # добавляем объект в группу сообщения
            message_list.append(pl) # добавляем объект в список сообщения, который нужен для передачи в шифрующую функцию
            messx += PL_W

    # обновляем все объекты группы сообщения (вызываем метод update)
    for i in message_group:
        i.update()

    for i in button_group:  # перебираем объекты группы кнопок управления
        i.update()  # вызывем для каждого объекта метод update
        if i.onClick(mouse_click):  # проверяем было ли нажатие по данной кнопке
            if i.text == 'Зашифровать': # если было нажатие и текст кнопки = Зашифровать
                message_list = encode() # то вызываем функцию шифрования
            if i.text == 'Стереть': #  если текст кнопки = Стереть
                # очищаем все группы кроме групп алфавита и кнопок управления
                message_group.empty()
                messx = 150 # задаем начальное положение отображения сообщения
                encode_message_group.empty()
                message_list = []   # обнуляем список объектов для дешифрования
                decode_message.empty()
            if i.text == 'Дешифровать': # если текст кнопки = Дешифровать
                decode(message_list)    # вызываем функцию дешифрования
            if i.text == 'Показать коды':   # если текст = Показать коды
                i.text = i.alt_text # меняем текст данной кнопки на альтернативный
                show_codes([message_group, encode_message_group, decode_message])   # вызываем функцию show_codes передавая ей все группы кнопок коды которых нужно показать
            elif i.text == 'Показать текст':    # если текст кнопки = Показать текст
                i.text = 'Показать коды'    # меняем основной текст на Показать коды
                show_text([message_group, encode_message_group, decode_message])    # вызываем функцию show_text и передаем ей все группы кнопок текст которых нужно отобразить

    #   обновляем все объекты группы зашифрованного сообщения (вызываем метод update)
    for i in encode_message_group:
        i.update()
    # обновляем все объекты группы дешифрованного сообщения (вызываем метод update)
    for i in decode_message:
        i.update()

    # отображаем поясняющие надписи
    screen.blit(ff.render('Алфавит', 1, Color('#fffc00')), (40, -3))
    screen.blit(ff.render('Сообщение: ', 1, Color('#fffc00')), (3,220))
    screen.blit(ff.render('Шифр:', 1, Color('#fffc00')), (3, 250))
    screen.blit(ff.render('Дешифр:', 1, Color('#fffc00')), (3, 280))

    # для каждой группы объектов вызываем метод draw для отрисовки их содержимого
    Alfavit.draw(screen)
    message_group.draw(screen)
    button_group.draw(screen)
    encode_message_group.draw(screen)
    decode_message.draw(screen)

    window.blit(screen, (0, 0))
    flip()