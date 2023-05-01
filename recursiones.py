def fibonacci(u):
    if u == 0:
        return 0
    elif u == 0:
        return 1
    else:
        return fibonacci(u-1) + fibonacci(u-2)


print(fibonacci(2))
