def func(num):
    if num == 0:
        return "ZeroDivisionError"
    elif type(num) != int:
        return "ValueError"
    else:
        return num / 100


print(func(input()))