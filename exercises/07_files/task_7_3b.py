# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = int(input('Enter VLAN number: '))
answer = "{:<10}{}{:>10}"

table = []

with open('CAM_table.txt') as f:
    for line in f:
        if "DYNAMIC" in line:
            line = line.split()
            table.append([int(line[0]),line[1],line[3]])

for i in sorted(table):
    if vlan in i:
        print(answer.format(i[0],i[1],i[2]))
