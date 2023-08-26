from scipy import integrate
import numpy as np 

epsilon = 8.85e-12
carga= 1.00e-6


def anillo(distancia, radio):

    cos= distancia/pow((distancia**2 + radio**2), 1/2)

    def f(s):
        return 1
    integral, error = integrate.quad(f, 0, (2 * np.pi * radio))
    dq = (carga / (2 * np.pi * radio)) * integral

    E = (1 / (4 * np.pi * epsilon)) * (dq / (distancia**2 + radio**2)) * cos

    print("El campo electrico es:", E, "N/C")

    return E

def lineal(largo, distancia):
    k = (1)/(4* np.pi * epsilon)
    lambda_ = carga / largo 

    def f(y):
        dL = 1  
        dQ = lambda_ * dL  
        return k * dQ * distancia / (distancia**2 + y**2)**(3/2)
    
    E, error= integrate.quad(f, -largo/2, largo/2)
    print("El campo electrico es:", E, "N/C")

    return E

def disco(distancia, radio):
    def f(r):
        return r/(((distancia**2) + (r**2))**(3/2))
    
    integral, error= integrate.quad(f, 0, radio)

    gama= (carga / (2 * np.pi * (radio**2)))

    E = ((gama * distancia)/(2 * epsilon)) * integral

    print("El campo electrico es:", E, "N/C")
    return E