import math

# -*- coding: utf-8 -*-
"""
Archivo: Simple.py
Descripción: Archivo de ejemplo en Python.
Autor: (Gary)
Fecha: 24/09/2025
"""
def main():
    print("Usa como variables n ")
    prop1= input("Ingrese tu primera proposicion")
    comp = input("Ingrese el comparador (=)")
    prop2= input("Ingrese tu segunda proposicion")
    var = input("Ingresa tu variable a utilizar en la proposicion")

    enun = Proposicion(prop1, comp, prop2, var)


#caso base

class Proposicion:
    def __init__(self, prop1, comp, prop2, var):
        self.prop1 = prop1
        self.comp = comp
        self.prop2 = prop2
        self.var = var
    
class casoBase(Proposicion):
    def __init__(self, prop1, comp, prop2, var):
        super().__init__(prop1, comp, prop2,var)

    def evaluar(self):
        pass
    
class hipotesisDeInduccion(Proposicion):
    def __init__(self, prop1, comp, prop2,var, varN1):
        self.varN1 = varN1
        super().__init__(prop1, comp, prop2,var)

    def Proposicion(self):
        pass
    
class pasoInductivo(Proposicion,hipotesisDeInduccion):
    def __init__(self, prop1, comp, prop2, varN1):
        super().__init__(prop1, comp, prop2, varN1)

    def evaluar(self):
        pass
    def comparar(self):
        pass