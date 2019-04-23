'''program ki izpise vsa prastevila do 200'''
def prastevila(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

    for i in range(2, 201):
        if prastevila(i):
            print(i)