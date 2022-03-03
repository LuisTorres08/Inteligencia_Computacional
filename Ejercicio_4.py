# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:13:21 2022

@author: ltorres49
"""

calificacion_1 = float(input('Ingrese la primera calificacion \n '))
calificacion_2 = float(input('Ingrese la segunda calificacion \n '))
calificacion_3 = float(input('Ingrese la tercera calificacion \n '))

talleres = calificacion_1 * 0.5
examen = calificacion_2 * 0.30
proyecto = calificacion_3 * 0.20

nota_final = talleres + examen + proyecto

print('Su calificacion final de fundamentos de programacion es: ', nota_final)