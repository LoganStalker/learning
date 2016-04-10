# -*- coding:utf-8 -*-

ALFAVIT = ('А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К',
           'Л','М','Н','О','П','Р','С','Т','У','Ф',
           'Х','Ц','Ч','Щ','Ш','Ъ','Ы','Ь','Э','Ю','Я','_',',','.')

message = 'МЕТОДЫ_ШИФРОВАНИЯ_С_СИММЕТРИЧНЫМ_КЛЮЧОМ'
print('Сообщение: %s'%message)

while 1:
    if len(message) % 8 != 0:
        print('\nДлина сообщения не кратна 8, добавляем *')
        message += '*'
        print(message)
    else:
        break

print('\nРазбиваем сообщение на блоки по 8 символов')
mess_blocks_list = []
for i in range(0, len(message), 8):
    mess_blocks_list.append(message[i:i+8])
print(mess_blocks_list)

print('\nШифруем сообщение')
K = [1,2,1,2,2]
L = 6
K_list = ((8,5,6,7,2,3,4,1), (1,8,7,2,3,6,5,4))
print('Ключ = %s \nДлина блоков зашифрованного сообщения = %s \nМаршруты: %s' % (K, L, K_list))
rez = []
for i in range(len(mess_blocks_list)):
    a = []
    mess = mess_blocks_list[i]
    for j in range(len(mess)):
        way = K_list[K[i]-1]
        a.append(mess[way[j]-1])
    print(i+1, '-й блок ', a)
    rez.append(a)

r = ''
for i in rez:
    for j in i:
        r += j

print('\nРазбиваем шифр на блоки длиной по %s символов'%L)
mess_blocks_list = []
for i in range(0, len(r), L):
    mess_blocks_list.append(r[i:i+L])
print(mess_blocks_list)