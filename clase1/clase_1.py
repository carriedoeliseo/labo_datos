#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:09:45 2024

@author: Estudiante
"""

# 9:00 - 12:00

''' Ejercicio, programa que decida si una palabra de longitud 5 es palindromo. '''

def palindromo (a):
    return a == a[::-1]

''' Ejercicio, programa que imporima en pantalla los numeros enteros entre 0 y 213 que sean divisibles por 13. '''

def ceromod13 ():
    i = 0
    while i <= 213:
        print(i)
        i += 13

''' Ejercicio, una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir de ahi cada dia vas y duplicás la 
cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea mas alta que el obelisco?
Datos, espesosr del billete: 0.11mm, altura del obelisco: 67.5m. '''

def billetemataobelisco ():
    ab = 0.11/1000
    dias = 1 
    while ab < 67.5:
        ab *= 2
        dias += 1
    return dias
