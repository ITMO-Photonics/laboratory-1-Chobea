import math
print('Height of a Cylinder H')
L = int(input())
print'Radius of a Cylinder R'
R = int(input())
def f(R,L):
	return math.pi * R * R * L
V = math.pi * R * R * L
print 'Volume of a Cylinder', V
print(f(R,L))
