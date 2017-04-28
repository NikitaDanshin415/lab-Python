import math
a = float(input("vvedite a = "))
y = float(input("vvedite y = "))
c = float(input("vvedite c = "))
x = float(input("vvedite x = "))


T=(a**5+(math.sin(y-c))**4/((math.sin(x+y))**3+abs(x-y)))

print(T)

