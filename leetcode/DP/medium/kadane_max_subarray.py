

def max_subarray(a, n):
    cur_max = a[0]
    max_sofar = a[0]

    for i in range(1, n):
        cur_max = max(a[i], cur_max + a[i])
        max_sofar = max(cur_max, max_sofar)

    return max_sofar

a = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(a)
print max_subarray(a, n)
