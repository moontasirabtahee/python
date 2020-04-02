def cube(num):
    x=num*num*num
    return x
def sq(num):
    return num*num
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y

p=int(input("Enter a num:"))
print(cube(p))
print(sq(p))
q=int(input("enter a another number:"))
print(add(p,q))
print(sub(p,q))
print(mult(p,q))