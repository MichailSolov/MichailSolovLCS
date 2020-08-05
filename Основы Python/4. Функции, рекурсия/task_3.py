def func(a):
    if len(a[1:]) > 1:
        d = {a[0]: func(a[1:])}
    else:
        d = {a[0]: a[len(a) - 1]}

    return d


print(func([1, 2, 3, 4]))
