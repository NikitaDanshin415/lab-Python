import math
b=2.2
c=3.7
a=round(math.sin(b),2)
x= round(a+(b+c)**3,2)
y = round(7*math.e**(math.sqrt(abs(x)))+(math.cos(x)**4),2)

print("a=",a)
print("x=",x)
print("y=",y)

