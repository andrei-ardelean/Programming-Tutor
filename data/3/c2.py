def sumaCifrelor(a):
    if a < 10:
        return a
    sum = 0
    while a > 0:
        sum = sum + a % 10
        a = a // 10
    return sum
