# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:24:33 2022

@author: ltorres49
"""

redes = int(input('Ingrese la cantidad de alumnos de redes \n'))
contabilidad = int(input('Ingrese la cantidad de alumnos de contabilidad \n'))
diseño = int(input('Ingrese la cantidad de alumnos de diseño \n'))

total = redes + contabilidad + diseño

porcentajes_redes = (redes / total) * 100
porcentajes_contabilidad = (contabilidad / total) * 100
porcentajes_diseño = (diseño / total) * 100

print('Porcentaje alumnos de redes: ' + str(porcentajes_redes) + '%')
print('Porcentaje alumnos de redes: ' + str(porcentajes_contabilidad) + '%')
print('Porcentaje alumnos de redes: ' + str(porcentajes_diseño) + '%')