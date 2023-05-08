def func(num):
    length = len(num)
    sum1 = 0
    sum2 = 0
    for i in range(0, length // 2):
        sum1 += int(num[i])
    for i in range(length // 2, length):
        sum2 += int(num[i])
    if sum1 == sum2:
        return True
    return False


print(func(input()))