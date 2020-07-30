from math import sqrt

data = input()
task_boolean = 0
KSqrt = sqrt(int(data.split(' ')[2]))

for i in range(1, int(KSqrt) + 1):
    if int(data.split(' ')[2]) % i == 0:
        if (i <= int(data.split(' ')[1]) and int(data.split(' ')[2]) / i <= int(data.split(' ')[0])) or \
                (i <= int(data.split(' ')[0]) and int(data.split(' ')[2]) / i <= int(data.split(' ')[1])):
            print("yes")
            task_boolean = 1
            break


if not task_boolean:
    print("no")
