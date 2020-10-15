

def isMatch(s, p):
    n = len(s)
    m = len(p)
    i, j =0, 0
    idx_i, idx_j = -1, -1

    while i < n:
        if j < m and s[i] == p[j]:
            i += 1
            j += 1
        elif j < m and p[j] == '*':
            idx_i = i
            idx_j = j
            j += 1
        elif idx_j != -1:
            j = idx_j + 1
            i = idx_i + 1
            idx_i += 1
        else:
            return False

    while j < m:
        if p[j] != '*':
            return False
        j += 1

    return True


print(isMatch("ababab", "a**b"))
print(isMatch("ababab", "a**ba"))
