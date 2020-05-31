

def subsets(ar):
    ans = [[]]

    for cur in ar:
        ans += [x+[cur] for x in ans]

    return ans


def subsets1(ar):
    ans = []
    n = len(ar)

    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]
        ans.append([ar[j] for j in range(n) if bitmask[j] == '1'] )
    return ans

print subsets1([1,2,3])
