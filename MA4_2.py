#!/usr/bin/env python3.9

from person import Person

import random
import math
import matplotlib.pyplot as pyplot
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future

from numba import njit

def fib_py(n):
    if n<= 1:
         return n
    else:
        return fib_py(n-1) + fib_py(n-2)
	
@njit
def fib_numba(n):
	if n<= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def main():
    
    if False:
        f = Person(50)
        print(f.getAge())
        print(f.getDecades())
        f.setAge(51)
        print(f.getAge())
        print(f.getDecades())

    if False: #plotta tiden för olika
        n = range(30, 45)
        y_py = []
        y_numba = []
        y_c = []
        
        for i in n:
            f=Person(i)
            t0 = pc()
            fib_py(i)
            t1 = pc()
            fib_numba(i)
            t2 = pc()
            f.fib()
            t3 = pc()
            
            y_py.append(t1-t0)
            y_numba.append(t2-t1)
            y_c.append(t3-t2)
            
        pyplot.plot(n, y_py, "r", label = "Python")
        pyplot.plot(n, y_numba, "g", label = "Python with Numba")
        pyplot.plot(n, y_c, "b", label ="C++")
        pyplot.xlabel("n")
        pyplot.ylabel("Time(s)")
        pyplot.savefig("fib_time.png")
        
    if True:
        n = range(20, 30)
        y_py = []
        y_numba = []
        
        
        for i in n:
            f=Person(i)
            t0 = pc()
            fib_py(i)
            t1 = pc()
            fib_numba(i)
            t2 = pc()
            
            
            y_py.append(t1-t0)
            y_numba.append(t2-t1)
           
            
        pyplot.plot(n, y_py, "r", label = "Python")
        pyplot.plot(n, y_numba, "g", label = "Python with Numba")
        
        pyplot.xlabel("n")
        pyplot.ylabel("Time(s)")
        pyplot.savefig("fib_time.png")
        

if __name__ == '__main__':
	main()
