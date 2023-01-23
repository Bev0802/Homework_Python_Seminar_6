''' - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
**44. Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.
Пример:
A (3,6); B (2,1) -> 5,09
A (7,-5); B (1,-1) -> 7,21'''

print("Введите координаты точки А")
ax = int(input("X: "))
ay = int(input("Y: "))

print("Введите координаты точки B")
bx = int(input("X: "))
by = int(input("Y: "))

## первый вариант
ab = lambda a, b: (a-b)**2
print (round(((ab(ax,bx)+ab(ay,by))**0.5), 3))
## второй вариант
print (round((((((lambda a, b: (a-b)**2)(ax,bx))+((lambda a, b: (a-b)**2)(ay,by)))**0.5)), 3))
