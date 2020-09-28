import math
print ("Задайте сторону треугольника а - ")
a = float(input())
print ("Задайте сторону треугольника б - ")
b = float(input())
print ("Введите величину угла между сторонами а и б (в градусах) - ")
x = float(input());
r = float(x*math.pi/180)
c = int((a*a+b*b-2*a*b*math.cos(r))**(1/2))
print ("Величина третей стороны -",c)


