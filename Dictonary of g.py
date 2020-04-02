def translator(x):
    p = ""
    for i in x:

        if i.lower( ) in "aeiou":
            p= p + "g"
        else:
            p= p + i
    return p

w=(translator(input("Enput a String:")))
print(w)