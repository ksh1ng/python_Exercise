def  letter_square(c,size):
    a=c*size
    for i in range(size-2):
        a=a+"\n"+c+" "*(size-2)+c
    a=a+"\n"+c*size
    return a

print(letter_square("w",7))
