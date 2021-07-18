def cmmdc(a, b):
    # a = abs(a)
    # b = abs(b)
    if a == 0:
        return a
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
