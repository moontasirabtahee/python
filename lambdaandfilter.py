def is_odd(x):
    if x%2!=0:
        return True

x=[2,3,4,5,67,7,8,6,5,4,3,4,5,6,7,7,8,89,6,6,5,4,43,2,1]
even = list(filter(lambda p:p%2==0,x))

odd =list(filter(is_odd,x))
print(x,even,odd)