
def lcs(X,Y, print_lcs=False):
  m = len(X)
  n = len(Y)
  L = [ [None]*(n+1) for _ in range(m+1) ]

  for i in range(m+1):
    for j in range(n+1):
      if i == 0 or j == 0:
        L[i][j] = 0
      elif X[i-1] == Y[j-1]:
        L[i][j] = 1 + L[i-1][j-1]
      else:
        L[i][j] = max(L[i-1][j],L[i][j-1])
  if print_lcs:
    printLCS(X,Y,L)
  return L[m][n]

def printLCS(X, Y, L):
  i = len(X)
  j = len(Y)
  lcs = []
  while i > 0 and j > 0:
    if X[i-1] == Y[j-1]:
      lcs.append(X[i-1])
      i -= 1
      j -= 1
    elif L[i-1][j] > L[i][j-1]:
      i -= 1
    else:
      j -= 1
  print "LCS: ", "".join(lcs[::-1])



# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print lcs(X, Y, print_lcs=True)