word = "win"
g=""
i = 0;
while g != word :
    g = input("Enter a word:")
    i+=1
    if word == g:
        print("You win")
        break
    else:
        print("you are wrong.try again")
    if i==5:
        print("You are out of time!")
        break