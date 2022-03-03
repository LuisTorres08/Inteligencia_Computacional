# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

donacion = float(input('Ingrese la donacion \n'))


administracion = donacion*0.35
sistemas = administracion*0.25
telecomunicaciones = sistemas*0.1
contabilidad = donacion - (telecomunicaciones + sistemas + administracion)

print('El valor que le corresponde a telecomunicaciones es:', telecomunicaciones)
print('El valor que le corresponde a sistemas es:', sistemas)
print('El valor que le corresponde a administracion es:', administracion)
print('El valor que le corresponde a contabilidad es:', contabilidad)