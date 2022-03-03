# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:00:07 2022

@author: ltorres49
"""

sueldo = float(input('Ingrese el sueldo \n'))
ventas = float(input('Ingrese las ventas por parte del vendedor \n '))

comision = ventas * 0.15
total = sueldo + comision

print('El valor total a paagar al vendedor es: ', total)
print('El valor ganado por comision es: ', comision)


