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

def lineal():
    return

def disco():
    return

E = anillo(4, 2, 2)
