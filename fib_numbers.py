

def fib(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    fib_num = (1, 1)
    for i in range(3, n+1):
        fib_num = (fib_num[1], fib_num[0] + fib_num[1])
    return fib_num[1]

print fib(3)
print fib(5)
