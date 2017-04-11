import math
y = float(input("vvedite y = "))
t = float(input("vvedite t = "))

a=(2.37*math.sin(t+1))/math.sqrt((4*y**2)-(0.1*y)+5)
print(a)