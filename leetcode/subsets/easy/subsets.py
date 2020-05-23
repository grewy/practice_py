def subsets_bitmap(arr):
    n = len(arr)
    ans = []

    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]
        ans.append([arr[j] for j in range(n) if bitmask[j] == '1'])
    return ans

def subsets(arr):
    ans = [[]]
    for ch in arr:
        ans += [cur + [ch] for cur in ans]
    return ans

print subsets([1,3,5])
print subsets_bitmap([1,3,5])
