#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math

## Calc Vertex
def calc_xv(a,b):
    return -b/(2*a)

def calc_yv(x,b,c):
    return x**2-abs(b)*x+c

###########################

# Calc cut-off points
def calc_cut_off_points(a,b,c):
    f1 = b**2-4*a*c
    f2 = 2*a
    
    x1 = (-b + math.sqrt(f1)) / f2
    x2 = (-b - math.sqrt(f1)) / f2
    return x1, x2

################################

# Calc Parabola
def calc_parabola(x,a,b,c):
    return a*x**2+b*x+c

def main(a, b, c):
    xv = calc_xv(a, b)
    yv = calc_yv(xv, b, c)

    # Range Points
    x = np.linspace(int(xv)-5,int(xv)+5,100)
    y = calc_parabola(x, a, b, c)

    # Print Points
    plt.plot(x,y)

    # Axis
    plt.axhline(y=0, color='black', linestyle='-')
    plt.axvline(x=0, color='black', linestyle='-')
    plt.savefig('./calc_img/calc.png')


main(5, -6, 5)

    
