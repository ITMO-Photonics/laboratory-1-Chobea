import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
x=np.linspace(0.1,2.4,100)
def f(x):
	return (np.cos(x)/(1+x*x))
root1 = optimize.bisect(f,0.1,2.4)
print (root1)
root2 = optimize.newton(f,1.5)
print (root2)
#root3 = optimize.newton(f,1.5,fprime=lambda x: -np.sin(x)*(1+x*x)-2*x*np.cos(x)/(1+x*x)**2)) - error
#print (root3)
root4 = optimize.brentq(f,0.1,2.4)
print (root4)
#%time optimize.newton(f,0)
