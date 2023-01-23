# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input('Введите подсеть: \n').split('.')
mask = str(ip[-1]).split('/')
mask1 = '1' * int(mask[-1]) + '0' * int(32 - int(mask[-1]))
m1,m2,m3,m4 = mask1[0:8], mask1[8:16], mask1[16:24], mask1[24:32]

output ="""
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""



print(output.format(int(ip[0]),int(ip[1]),int(ip[2]),int(mask[0])))
print('Mask:')
print('/',mask[-1],sep='')
print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(int(m1,2),int(m2,2),int(m3,2),int(m4,2)))
print("{0:<10}{1:<10}{2:<10}{3:<10}".format(m1,m2,m3,m4))

