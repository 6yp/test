#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt', 'r') as f:
    for line in f:
        line = (line.rstrip().split())
        print(f'''{'Protocol:':20}{'OSPF':<10}
{'Prefix:':20}{line[1]:<10}
{'AD/Metric:':20}{line[2].strip('[]')}
{'Next-Hop:':20}{line[4].rstrip(',')}
{'Last update:':20}{line[5].rstrip(',')}
{'Outbound Interface:':20}{line[6]}
''')
