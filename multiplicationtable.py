import string
def multiple(n):
    row = ''

    for i in range(1,13):
        row += str(i) + "*" + str(n) + " = " + str(i*n) + "\t"
    
    print(row.ljust(3))


for j in range(1,13):
    multiple(j)
