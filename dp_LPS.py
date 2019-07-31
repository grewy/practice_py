from dp_lcs import lcs

def lps(a):
  b= a[::-1]
  return lcs(a, b)

# Driver program to test above functions
seq = "GEEKS FOR GEEKS"
n = len(seq)
print("The length of the LPS is " + str(lps(seq)))