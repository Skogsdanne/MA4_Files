#!/usr/bin/env python3.9

"""
Student: Daniel Nilsson 
Mail: d.nilsson1998@gmail.com
Reviewed by: Nasser
Reviewed date: 5/10
"""


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

    if True: #plotta tiden för olika
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
        pyplot.yscale('log')
        pyplot.xlabel("n")
        pyplot.ylabel("Time(s)")
        pyplot.savefig("30_45fib.png")
        
    if False:
        n = range(20, 30)
        y_py = []
        y_numba = []
        #Numba tar extra tid första loopen för den ska
        #kompilera allt först eller nåt
        
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
        pyplot.savefig("20_30fib.png")
        
    if False:
        n = 47
        f = Person(n)
        print(f.fib(), "n = 47 och C++")
        print(fib_numba(n), "n = 47 och Numba")
        #-1323752223 n = 47 och C++
        #2971215073 n = 47 och Numba
        #antar c++ får nån knas int overflow?
        #yes, 2147483647 är max integer i c++
if __name__ == '__main__':
	main()
