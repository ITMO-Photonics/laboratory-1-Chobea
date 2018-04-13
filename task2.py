import numpy as np
#import timeit
from scipy import optimize

x=np.linspace(0.1,2.4,100)
def f(x):
	return (np.cos(x)/(1+x*x))
def fprime(x):
	return (-np.sin(x)*(1+x*x)-2*x*np.cos(x))/((1+x*x)**2)

print ('Bisection method')
root1 = optimize.bisect(f,0.1,2.4)
print (root1)
#%timeit optimize.newton(f,0.1,2.4)

print('Newton-Raphson method')
root2 = optimize.newton(f,1.5)
print (root2)

print('Secant method')
root3 = optimize.newton(f,1.5,fprime)
print (root3)

print('Brents method')
root4 = optimize.brentq(f,0.1,2.4)
print (root4)

