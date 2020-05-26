#   Calculo Numerico (SME0602) - Projeto Pratico 1 - Metodo de Halley
#   Alunos: Leandro Silva, Marianna Karenina, Marilene Garcia
#
#   Para rodar (no terminal linux): python halley.py

import math
import numpy as np

def halley( f, x0, e ):
    x = []
    x.append(x0)

    der_f = f_der(f,x0)
    der2_f = f_der2(f,x0)
    x_now = x0 - (f(x0)*der_f)/(pow(der_f,2)-0.5*f(x0)*der2_f)
    x_previous = x0

    while abs(x_now - x_previous) > e:
        if(f_der(f,x_now) != 0):
            x_next = x_now - (f(x_now)*der_f)/(pow(der_f,2)-0.5*f(x_now)*der2_f)

        x.append(x_now)
        x_previous = x_now
        x_now = x_next
        der_f = f_der(f,x_now)
        der2_f = f_der2(f,x_now)

    return x

def f1( x ):
    return math.cos(x)

def f2( x ):
    return x/2 - 2

def f_der( f, x ):
    h = 1e-5
    return (f(x+h)-f(x-h))/(2*h)

def f_der2( f, x ):
    h = 1e-5
    return (f_der(f,x+h)-f_der(f,x-h))/(2*h)  

def main(): 

    #print( halley(f1,45,0.000001) )
    
    print( halley(f2,4575,0.000001) )


if __name__ == "__main__":
    main()
