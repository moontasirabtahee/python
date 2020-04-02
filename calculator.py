from math import *
while True:
    def add(x, y):
        print(x + y)


    def sub(x, y):
        print(x - y)


    def mult(x, y):
        print(x * y)


    def divi(x, y):
        print(x / y)


    def sq(x):
        print(x * x)


    def cube(x):
        print(x * x * x)


    p = float(input("input a number:"))
    y = input("Enter a operator from the list \n1)+\n2)-\n3)*\n4)/\n5)x^2\n6)x^3 \nyour oprator")
    if y == ('x^2') or y == ('x^3') or y == '5' or y == '6':
        if y == ('x^2') or y == '5':
            sq(p)
        else:
            cube(p)
    else:
        z = float(input("Enter an another number:"))
        if y == '+' or y == '1':
            add(p, z)
        elif y == '-' or y == '2':
            sub(p, z)
        elif y == '*' or y == '3':
            mult(p, z)
        elif y == '/' or y == '4':
            divi(p, z)

