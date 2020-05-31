

def subsets_dup(ar):
    ans = [[]]

    if not ar:
        return []

    ar.sort()

    cur = []

    for i in range(len(ar)):
        if i > 0 and ar[i] == ar[i-1]:
            cur = [c+[ar[i]] for c in cur]
        else:
            cur = [c+ [ar[i]] for c in ans]
        ans += cur

    return ans

a = [1,2,2]
print subsets_dup(a)
