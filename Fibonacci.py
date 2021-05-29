def Fb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return Fb(n-1) + Fb(n-2)

