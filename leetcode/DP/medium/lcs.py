"""
L[i][j] : LCS of X[0-(i-1)] and Y[0-(j-1)]

1. last char of sequences equal :
        L(x,y) = 1 + L(x[-1], y[-1])
2. last not equal, last elemnt of only one of the sequence is taken:
        L(x,y) = max(L(x,y[-1]), L(x[-1],y))
"""

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print "Length of LCS is ", lcs(X, Y)
