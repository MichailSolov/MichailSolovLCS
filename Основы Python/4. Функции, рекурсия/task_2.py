def func(n):
    if n > 0:

        if n == 2 or n == 1:
            return 1
        else:
            return func(n - 1) + func(n - 2)


print(func(6))
