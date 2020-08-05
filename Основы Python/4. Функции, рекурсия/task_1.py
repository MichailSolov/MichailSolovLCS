def func(n):
    if n > 0:
        return n * func(n - 1)
    else:
        return 1


print(func(int(input("enter the num "))))
