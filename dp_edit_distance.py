def editDistDP(str1, str2, m, n):
  # Create a table to store results of subproblems
  dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

  for i in range(m):
    dp[i][0] = i
  for j in range(n):
    dp[0][j] = j

  for i in range(1, m+1):
    for j in range(1, n+1):
      if str1[i-1] == str2[j-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = 1 + min(dp[i][j-1],         # Insert
                           dp[i-1][j],          # Remove
                           dp[i-1][j-1])       # Replace

  return dp[m][n]


# Driver program
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))