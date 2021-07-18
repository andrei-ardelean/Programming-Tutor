def sumaCifrelor(a):
    sum = 0
    while a > 0:
        sum = sum + a % 10
        a = a // 10
    return sum
