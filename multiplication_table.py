def multiple(n):
    row = ''

    for i in range(1,13):
        row += str(i*n)+"\t "
    return row

for j in range(1,13):
    print(multiple(j))
