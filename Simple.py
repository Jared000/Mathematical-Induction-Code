import math

# -*- coding: utf-8 -*-
"""
Archivo: Simple.py
Descripción: Archivo de ejemplo en Python.
Autor: (Gary)
Fecha: 24/09/2025
"""
#caso base

class Proposicion:
    def __init__(self, prop1, comp, prop2, var):
        self.prop1 = prop1
        self.comp = comp
        self.prop2 = prop2
        self.var = var
    
    def __str__(self):
        return f"{self.prop1} {self.prop2}, con variable {self.var}"
    
class casoBase(Proposicion):
    def __init__(self, prop1, comp, prop2, var):
        super().__init__(prop1, comp, prop2,var)

    def lecture(self):
        lec1 =[] 
        for i in self.prop1:
            lec1.append("1" if i == "n" else i)

        lec2 = []
        for i in self.prop2:
            lec2.append("1" if i == "n" else i)

        self.evaluar(lec1, lec2)
        
    
    def evaluar(self,lec1,lec2):
            exp1 = "".join(lec1)
            exp2 = "".join(lec2)


            ec1 = eval(exp1)
            ec2 = eval(exp2)

            if ec1 == ec2:
                print("Caso Base confirmado !!!")
            else:
                print("Demostracion no valida")

class hipotesisDeInduccion(Proposicion):
    def __init__(self, prop1, comp, prop2,var, varN1):
        self.varN1 = varN1
        super().__init__(prop1, comp, prop2,var)


    def Proposicion(self):
        pass
    
class pasoInductivo(hipotesisDeInduccion):
    def __init__(self, prop1, comp, prop2, varN1):
        super().__init__(prop1, comp, prop2, varN1)

    def evaluar(self):
        pass
    def comparar(self):
        pass




def main():
    print("Usa como variables n ")
    prop1= input("Ingrese tu primera proposicion ")
    comp = input("Ingrese el comparador (=) ")
    prop2= input("Ingrese tu segunda proposicion ")
    var = input("Ingresa tu variable a utilizar en la proposicion ")

    enun = Proposicion(prop1, comp, prop2, var)
    print("\n Proposicion general:", enun)

    caseB = casoBase(prop1, comp, prop2,var)
    caseB.lecture()
    #caseB.evaluar()

if __name__ == "__main__":
    main()