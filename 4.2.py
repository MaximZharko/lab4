def func(num):
    if not num.isdigit():
        return "ValueError"
    elif int(num) == 0:
        return "ZeroDivisionError"
    else:
        return 100 / int(num)


print(func(input()))