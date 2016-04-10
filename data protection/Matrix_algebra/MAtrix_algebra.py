# -*- coding:utf-8 -*-

alfavit = ("а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р",
           "с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","_")

message = tuple("матричная_алгебра")
key = ((1,3,5),(2,6,9),(7,4,8))

print('Формируем список чисел эквивалентных буквам алфавита')
a = []
for i in message:
    ind = alfavit.index(i)+1
    a.append(ind)
print(a)

while 1:
    if len(a)%3 != 0:
        a.append(0)
        print('\nДлина списка нечетное число, поэтому добавляем в список 0')
        print(a)
    else:
        break

print('\nШифруем сообщение')
rez = []
for i in range(0, len(a), 3):
    prom = []
    for key_line in key:
        code_digit = key_line[0]*a[i]+key_line[1]*a[i+1]+key_line[2]*a[i+2]
        rez.append(code_digit)

print('Полученный шифр: ', rez)