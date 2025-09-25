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

#caso base

class Proposicion:
    def __init__(self, prop1, comp, prop2):
        self.prop1 = prop1
        self.comp = comp
        self.prop2 = prop2

    def evaluar(self):
        if self.comp == "=":
            return self.prop1 == self.prop2
        else:
            raise ValueError("Comparador no válido")

class lecturaDeProposicion(Proposicion):
    def __init__(self, prop1, comp, prop2):
        super().__init__(prop1, comp, prop2)

    def evaluar(self):
        return super().evaluar()
    
class casoBase(Proposicion):
    def __init__(self, prop1, comp, prop2):
        super().__init__(prop1, comp, prop2)

    def evaluar(self):
        return super().evaluar()
    
class hipotesisDeInduccion(Proposicion):
    def __init__(self, prop1, comp, prop2):
        super().__init__(prop1, comp, prop2)

    def evaluar(self):
        return super().evaluar()
    
class casoInductivo(Proposicion):
    def __init__(self, prop1, comp, prop2):
        super().__init__(prop1, comp, prop2)

    def evaluar(self):
        return super().evaluar()