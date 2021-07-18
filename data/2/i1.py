def concat(x, y):
    z = []
    while x != [] and y != []:
        if x[0] < y[0]:
            z.append(x[0])
            x = x[1:]
        else:
            z.append(y[0])
            y = y[1:]
    if len(x) == 0:
        z.append(y)
    if len(y) == 0:
        z.append(x)
    return z
