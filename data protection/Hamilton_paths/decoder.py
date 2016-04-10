# -*- coding:utf-8 -*-

ALFAVIT = ('А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К',
           'Л','М','Н','О','П','Р','С','Т','У','Ф',
           'Х','Ц','Ч','Щ','Ш','Ъ','Ы','Ь','Э','Ю','Я','_',',','.')

mess = ['КРГРИО',   'ТПОЕСК',  'ФИЧАРЕ',  'ОБ_ПРЕ',   'АЕИЗОН',   'АВ_АМИ',   'НРОФ**',   '**ИИ*Ц']
#mess = ['ШДЫ_ЕТ', 'ОМИИНФ', 'РАВОМС', 'ИМ_С_Я', 'ЕМЫТРН', 'ЧИ_*МК', 'ЛОЧЮ']
print('Исходное сообщение блоками: %s'%mess)
message = ''
for i in mess:
    message += i
print('Исходное сообщение строкой: %s'%message)

print('\nРазбиваем сообщение на блоки по 8 символов')
mess_blocks_list = []
for i in range(0, len(message), 8):
    mess_blocks_list.append(message[i:i+8])
print(mess_blocks_list)

print('\nДешифруем сообщение')
#K = [1,2,1,2,2]
K = [2,1,1,2,2,1]
K_list = [[8,5,6,7,2,3,4,1], [1,8,7,2,3,6,5,4]]
print('Ключ = %s \nМаршруты: %s' % (K, K_list))
rez = []
for i in range(len(mess_blocks_list)):
    a = [0,]*8
    mess = mess_blocks_list[i]
    for j in range(len(mess)):
        way = K_list[K[i]-1]
        a[way[j]-1] = mess[j]
    print(i+1, '-й блок ', a)
    rez.append(a)

print('\nУбираем из сообщения дополнительные символы, если такие имеются...')
r = ''
for i in rez:
    for j in i:
        if j != '*':
            r += j
print('\nРасшифрованное сообщение: %s' % r)