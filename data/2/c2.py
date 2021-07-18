def concat(x, y):
    z = x + y
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(z) - 1):
            if z[i] > z[i+1]:
                z[i], z[i+1] = z[i+1], z[i]
                swapped = True
    return z
