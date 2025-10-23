import math
x = 0.4 * math.pow(10, 4)
y = -0.875
z = -0.475*math.pow(10, -3)
s = math.pow(abs(math.cos(x)-math.cos(y)), (1+2*math.sin(y)*math.sin(y))) * (1 + z + z**2/2 + z**3/3 + z**4/4)
print(s)