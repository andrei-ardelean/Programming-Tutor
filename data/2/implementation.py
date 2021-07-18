def concat(x,y):
    result = []
    i=0
    j = 0

    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1

    result = result + x[i:] + y[j:]

    return result
