from scipy import integrate
import numpy as np 

epsilon = 8.85e-12


def anillo(distancia, radio, carga):

    cos= distancia/pow((distancia**2 + radio**2), 1/2)

    def f(s):
        return 1
    integral, error = integrate.quad(f, 0, (2 * np.pi * radio))
    dq = (carga / (2 * np.pi * radio)) * integral

    E = (1 / (4 * np.pi * epsilon)) * (dq / (distancia**2 + radio**2)) * cos

    print("El campo electrico es:", E)

    return E

def lineal(largo, distancia, carga):
    r= distancia**2 + largo**2
    cos = distancia/(r**1/2)
    sen = largo/(r**1/2)

    def f(s):
        return 1
    media= largo/2
    integral, error= integrate.quad(f, -media, media)

    lam= carga/largo
    r= distancia**2 + largo**2

    Ex= (1 / (4 * np.pi * epsilon)) * (lam/r) * cos * integral
    print("El campo electrico es:", Ex)

    return Ex

def disco(distancia, radio, carga):
    def f(r):
        return r/((distancia**2 + r**2)**3/2)
    
    integral, error= integrate.quad(f, 0, radio)

    gama= (carga / (2 * np.pi * (radio**2)))

    E = ((gama * distancia)/(2 * epsilon)) * integral

    print("El campo electrico es:", E)
    return

E = lineal(4, 3, 2)
