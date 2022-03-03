# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:40:37 2022

@author: ltorres49
"""

persona_1 = float(input('Cantidad de dinero a invertir primera persona \n'))
persona_2 = float(input('Cantidad de dinero a invertir primera personar \n'))
persona_3 = float(input('Cantidad de dinero a invertir primera persona \n'))

total_inversion = persona_1 + persona_2 + persona_3

porcentaje_persona1 = (persona_1 / total_inversion) * 100
porcentaje_persona2 = (persona_2 / total_inversion) * 100
porcentaje_persona3 = (persona_3 / total_inversion) * 100

print('Porcentaje que invierte la primera persona: ' + str(round(porcentaje_persona1,2)) + '%')
print('Porcentaje que invierte la primera persona: '+ str(round(porcentaje_persona2,2)) + '%')
print('Porcentaje que invierte la primera persona: '+ str(round(porcentaje_persona3,2)) + '%')