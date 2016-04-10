# -*- coding:utf-8 -*-

alfavit = ("а","б","в","г","д","е","ж","з","и","к","л","м","н","о","п","р",
           "с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я","_")

#message = (105, 192, 232, 158, 293, 332, 171, 311, 343, 90, 169, 316, 32, 62, 68, 19, 38, 116)
#key = ((1,3,5),(2,6,9),(7,4,8))
message = (55, 97, 126, 118, 199, 287, 122, 246, 264, 54, 159, 230, 155, 279, 124)
key = ((5, 1, 3),(9, 6, 2),(4, 7, 8))

print('Вычисляем определитель матрицы ключа A')
a, b, c = 0, 1, 2
mod = key[a][0]*key[b][1]*key[c][2] + key[a][1]*key[b][2]*key[c][0] + key[a][2]*key[b][0]*key[c][1] - key[a][2]*key[b][1]*key[c][0] - key[a][1]*key[b][0]*key[c][2] - key[a][0]*key[b][2]*key[c][1]
print('|A| = ', mod)

print('\nВычисляем союзную матрицу A*')
print('A* = ')
sojuznaja = []
for i in range(3):
    sojuznaja.append([0, 0, 0])
for i in range(3):
    for j in range(3):
        a = []
        for x in range(3):
            for y in range(3):
                if x != i:
                    if y != j:
                        a.append(key[x][y])
        sojuznaja[i][j] = a[0]*a[3]-a[1]*a[2]
sojuznaja[0][1] *= -1
sojuznaja[1][0] *= -1
sojuznaja[1][2] *= -1
sojuznaja[2][1] *= -1
for i in sojuznaja:
    print(i)

print('\nТранспонируем матрицу A*')
print('A(t) = ')
transponirovan = []
for i in range(3):
    prom = []
    for j in range(3):
        prom.append(sojuznaja[j][i])
    transponirovan.append(prom)
for i in transponirovan:
    print(i)

print('\nНаходим обратную матрицу матрицы At по формуле A(обратная) = A(t)/|A|')
print('A(обратная) = ')
sojuznaja = []
for i in transponirovan:
    prom = []
    for j in i:
        prom.append(j / mod)
    sojuznaja.append(prom)
    print(prom)

print('\nРезультат: ')
rez = []
for i in range(0, len(message), 3):
    prom = []
    for key_line in sojuznaja:
        code_digit = key_line[0]*message[i]+key_line[1]*message[i+1]+key_line[2]*message[i+2]
        rez.append(round(code_digit))
print(rez)

message = ''
for i in rez:
    message += alfavit[i-1]
print('Расшифрованное сооьбщение:', message)