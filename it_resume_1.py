def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def easy_num(num):
    for i in range(1, num):
        if i == 1:
            continue
        if num % i == 0:
            return False
    return True


def operation(num, count):
    n = 1
    case = 1
    while (num // count ** n) > count:
        if num % (count ** n) == 0:
            case = n
        n += 1
    return case


def result(num):
    res_str = []
    f = factorial(num)
    count = 2
    while f != 1:
        if easy_num(count):
            h = operation(f, count)
            f /= (count ** h)
            if h > 1:
                res_str.append(f'{count}^{h}')
            else:
                res_str.append(f'{count}')
        count += 1
    return ' * '.join(res_str)


print(result(22))
