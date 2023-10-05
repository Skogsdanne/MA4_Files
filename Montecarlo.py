"montecarlo"
"""
Student: Daniel Nilsson 
Mail: d.nilsson1998@gmail.com
Reviewed by: Nasser
Reviewed date: 5/10
"""

import random
import math
import matplotlib.pyplot as pyplot
from time import perf_counter as pc
import concurrent.futures as future

def montecarlo(n):
    x = []
    y = []
    color = []
    nc = 0 
    for i in range(n):
        y.append(random.uniform(-1, 1)) #lägger till slumpade nummer i vektorerna
        x.append(random.uniform(-1,1))
        
        if x[i]**2 + y[i]**2 <= 1:
            nc += 1
            color.append([1,0,0])
        else:
            color.append([0,0,1])
            
    pyplot.scatter(x,y, c = color) #gör plot med färgvektorn som argument för färg
    print('n:', n, 'nc:', nc, ', uppskattat pi:', 4*nc/n, ', pi:', math.pi, )
    return 4*nc/n

def hypersphere(n, d): 
    
    def lessthanone(radie): #kollar bara om r är mindre än 1
        if radie <= 1:
            return True
        else:
            return False

    #list comprehension. stoppar in alla kvadraterna i en lista
    radii = [sum([random.uniform(-1, 1)**2 for d in range(d)]) for i in range(n)]
    
    #filter
    c = len(list(filter(lessthanone, radii))) #filtrerar bort alla med r över 1
    
    print('dimensioner:', d,', samples:', 'nc: ', c,'approx: ', 2**d*(c/n))
    return 2**d*(c/n)

def hypersphere_exact(d): #lite onödigt användande av lambda men gott nog
    f = lambda x: math.pi**(x/2) / (math.gamma(x/2 + 1))
    print('dimensioner: ', d,', exakt hypersfär:', f(d))
    return f(d)

def hypersphere_paralell(n, d, proc):
    with future.ProcessPoolExecutor() as PPE:
        processes = []
        result = []
        npp = n//proc
        for i in range(10): #gör 10 processer
            p = PPE.submit(hypersphere, npp, d)
            processes.append(p)
        for p in processes:
            result.append(p.result())
            
    print('hypersphere_paralell','dimensioner:', d, ', samples:', n,', processes: ', proc, ', approx: ', sum(result)/proc)
    return sum(result)/proc


def main():
    if True:
        montecarlo(1000)
        pyplot.savefig('MonteCarlo_1k.png')
        montecarlo(10000)
        pyplot.savefig('MonteCarlo_10k.png')
        montecarlo(100000)
        pyplot.savefig('MonteCarlo_100k.png')
        #n: 1000 nc: 783 , uppskattat pi: 3.132 , pi: 3.141592653589793
        #n: 10000 nc: 7885 , uppskattat pi: 3.154 , pi: 3.141592653589793
        #n: 100000 nc: 78495 , uppskattat pi: 3.1398 , pi: 3.141592653589793""""""
    if False: #1.2 och 1.3
        n = 10000000
        d = 11

        t0 = pc()
        print('Serial')
        hypersphere(n, d)
        t1 = pc()
        print('Parallell')
        hypersphere_paralell(n, d, 10)
        t2 = pc()

        hypersphere_exact(11)
        print(f'Seriel time: {round(t1-t0,2)}s')
        print(f'Parallell tid: {round(t2-t1,2)}s')

""        
#Serial
#dimensioner: 11 , samples: nc:  9128 approx:  1.8694144
#Parallell
#dimensioner: 11 , samples: nc:  943 approx:  1.931264
#dimensioner: 11 , samples: nc:  871 approx:  1.783808
#dimensioner: 11 , samples: nc:  918 approx:  1.880064
#dimensioner: 11 , samples: nc:  889 approx:  1.820672
#dimensioner: 11 , samples: nc:  940 approx:  1.92512
#dimensioner: 11 , samples: nc:  959 approx:  1.964032
#dimensioner: 11 , samples: nc:  1002 approx:  2.052096
#dimensioner: 11 , samples: nc:  938 approx:  1.921024
#dimensioner: 11 , samples: nc:  865 approx:  1.77152
#dimensioner: 11 , samples: nc:  885 approx:  1.81248
#hypersphere_paralell dimensioner: 11 , samples: 10000000 , processes:  10 , approx:  1.8862079999999999
#dimensioner:  11 , exakt hypersfär: 1.8841038793898994
#Seriel time: 45.29s
#Parallell tid: 12.91s""
        
if __name__ == '__main__':
	main()