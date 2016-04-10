# -*- coding:utf-8 -*-

def input_key_and_message(): # процедура ввода ключа и сообщения
    message = input('Введите сообщение: ')
    if len(message) % 2 != 0:   # проверяем длину сообщения, так как сообщение будет при шифровании разбиваться на биграммы, необходимо чтобы в сообщении было четное количество символов.
        message += 'ь'          # в сообщении легко будет понять где лишний символ, если там будет мягкий знак
    message = message.lower()   # переводим сообщение в нижний регистр

    key = tuple(input('Введите ключ: '))    # input получает сообщение (в данном случае это ключ), tuple разбивает ключ на символы и возвращает кортеж
    message = tuple(message)                # разбиваем сообщение на символы

    return key, message # передаем результат

def make_table(key, alfavit):   # создаем таблицу шифрования
    key += alfavit  # объединяем ключ и алфавит в один

    alfavit = []
    for i in key:
        if i not in alfavit:
            alfavit.append(i) # формируем новый алфавит, в котором отбрасываем повторяющиеся символы

    table = []  # будущая таблица
    a = []  # список а - в данном случае это строка таблицы table
    for i in alfavit: # В данном цикле формируем таблицу шифрования
        a.append(i) # добавляем символы в список а
        if (alfavit.index(i)+1) % 8 == 0:   # когда длина списка а становится равной 6
            table.append(a)                 # добавляем список в таблицу
            a = []                          # а потом обнуляем этот список
        if alfavit.index(i) == len(alfavit)-1:
            table.append(a)

    for i in table: # выводим строки таблицы
        print(i)

    return table    # передаем таблицу

def find_index(simbol, table):  # в данной процедуре определяем индекс символа
    for table_row in table: # в цикле перебираем строки таблицы
        col = 0 # это номер столбца
        row = 0 # это номер строки
        if simbol in table_row: # если искомый символ в данной строке,
            col = table_row.index(simbol)   # то определяем номер искомого символа в данной строке
            row = table.index(table_row)         # потом определяем номер данной строки в таблице
            break   # прекращаем выполнение цикла
    return col, row # передаем результаты

def encrypt(table, message):    # процедура шифрования
    rez = []
    for i in range(1, len(message), 2): # в цикле перебираем каждый второй индекс начиная с 1
        b = message[i]  # берем из сообщения i-й символ
        a = message[i-1]    # берем из сообщения (i-1)-й символ
        acol, arow = find_index(a, table)   # определяем индексы столбца и строки в которых расположен символ A
        bcol, brow = find_index(b, table)   # определяем индексы столбца и строки в которых расположен символ B
        if acol == bcol:    # если символы в одном столбце, то их по правилу шифрования заменяют символами расположенными в следующей строке
            ccol, crow = acol, arow+1   # задаем индексы символа С, на основе индексов символа A, к индексу строки при этом прибавляем 1, для сдвига на следующую строку
            dcol, drow = bcol, brow+1   # задаем индексы символа D, на основе индексов символа B, к индексу строки при этом прибавляем 1, для сдвига на следующую строку
            if crow == len(table):  # если индекс строки равен количеству строк в таблице (а нумерация в Python начинается с нуля, значит фактически индекс превышает допустимое значение),
                crow = 0            # то обнуляем иднекс строки, отправляя его к первой строке
            if drow == len(table):  # и то же самое делаем с индексом строки для символа D
                drow = 0
        elif arow == brow:  # если символы расположены в одной строке, то их по правилу шифрования нужно заменить символом справа
            ccol, crow = acol+1, arow   # задаем индексы символа C на основе индексов символа A, к индексу столбца при этом прибавляем 1, для сдвига вправо
            dcol, drow = bcol+1, brow   # аналогично задаем индексы символа D.
            if ccol == len(table[0]):   # если индекс равен количеству столбцов (так как нумерация в Python начинается с нуля, то индекс в этом случае фактически будет выше допустимого значения)
                ccol = 0                # то обнуляем его, отправляя к первому столбцу
            if dcol == len(table[0]):   # далее аналогичная логика
                dcol = 0
        else:   # если же не выполняется ни одно условие,
            ccol, crow = bcol, arow # то задав определенные индексы получим координаты символов из противоположных углов прямоугольника шифрования (читайте о шифре Плейфера)
            dcol, drow = acol, brow #

        c = table[crow][ccol]   # по полученным координатам извлекаем из таблицы символ C
        d = table[drow][dcol]   # по полученным координатам извлекаем из таблицы символ D

        rez.append(c)   # добавляем символы в список rez
        rez.append(d)

    return rez # возвращаем результат работы функции/процедуры... вроде нет разницы. Или есть - функция ни чего не возвращает, а процедура возвращает. Надо загуглить...

def main(): # главная функция
    print('Шифр Плейфера')

    alfavit = ("а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р",
           "с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","_")
    #alfavit = ("а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р",
    #       "с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"," ",",",".")

    # с помощью созданных выше процедур и функций задаем сообщение с ключем, обрабатываем и шифруем
    key, message = input_key_and_message()
    table = make_table(key, alfavit)
    rez = encrypt(table, message)

    print(message) # выводим сообщение списком
    print(rez)      # выводим результат списком

    # ниже склеиваем символы из списка rez в одну строку и получаем зашифрованное сообщение
    message = ''
    for i in rez:
        message += i
    print(message)

if __name__ == '__main__':  # вызываем главную функцию
    main()