# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите IP-адрес:\n')
ip_oct = ip.split('.')
right = True

if len(ip_oct) != 4:
    right = False
else:
    for i in ip_oct:
        if i.isdigit() != True or int(i) not in range(256):
            right = False
            break

                
if right == False:
    print('Неправильный IP-адрес')
else:
    if 1 <= int(ip_oct[0]) <= 223:
        print('unicast')
    elif 224 <= int(ip_oct[0]) <= 239:
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassgined')
    else:
        print('unused')
