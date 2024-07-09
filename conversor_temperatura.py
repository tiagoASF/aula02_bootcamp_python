#!/usr/bin/env python

""" Conversor de temperatura """
__version__ = "0.1.0"
__author__ = "Tiago Fialho"

import math

temperatura_celsius = float(input("Informe a temperatura em Celcius: "))
escala_para_conversao = input("Converter para Fahrenheit(F) ou Kelvin(K): ")
temperatura_convertida = "" 

if (escala_para_conversao.lower() == 'k'):
    temperatura_k = temperatura_celsius + 273
    temperatura_convertida = str(temperatura_k) + "K" 
elif (escala_para_conversao.lower() == 'f'):
    temperatura_f = (temperatura_celsius * 1.8) + 32
    temperatura_convertida = str(temperatura_f) + "ºF"

print(f"{temperatura_celsius}º equivalem a {temperatura_convertida}")