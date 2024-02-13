def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def res(n):
    chs = 1
    for i in range(1, n + 1):
        chs = chs * i // zm(chs, i)
    return chs

def zm(a, b):
    while b != 0:
        a, b = b, a % b

    return a