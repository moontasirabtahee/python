while True:
    n = [0,1]
    x = int(input("how many fibonacci number do u want :"))
    for i in range(x):
        n.append(n[-1]+n[-2])

    print(n)
    print("bye")