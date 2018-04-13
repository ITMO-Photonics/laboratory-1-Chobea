import numpy as np
import timeit
from scipy import optimize

x=np.linspace(0.1,2.4,100)
def f(x):
	return (np.cos(x)/(1+x*x))
def fprime(x):
	return (-np.sin(x)*(1+x*x)-2*x*np.cos(x))/((1+x*x)**2)

print ('Bisection method')
start = timeit.default_timer()
root1 = optimize.bisect(f,0.1,2.4)
stop = timeit.default_timer()-start
print (root1)
print(stop)

print('Newton-Raphson method')
start = timeit.default_timer()
root2 = optimize.newton(f,1.5)
stop = timeit.default_timer()-start
print (root2)
print(stop)

print('Secant method')
start = timeit.default_timer()
root3 = optimize.newton(f,1.5,fprime)
stop = timeit.default_timer()-start
print (root3)
print(stop)

print('Brents method')
start = timeit.default_timer()
root4 = optimize.brentq(f,0.1,2.4)
stop = timeit.default_timer()-start
print (root4)
print(stop)

