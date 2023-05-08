def func(date):
    flag = False
    num1 = 0
    num2 = 0
    num3 = 0
    word = ""
    for sym in date:
        if sym == '.':
            if flag == 0:
                num1 = int(word)
                flag = True
            elif flag == 1:
                num2 = int(word)
            word = ""
        else:
            word += sym
    num3 = int(word) % 100
    if num1 * num2 == num3:
        return True
    return False


print(func(input()))
