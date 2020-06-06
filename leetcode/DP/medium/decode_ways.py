"""
"12121"
Length 1: "1" => [1]
Length 2: "12" =>[1,2] [12]
Length 3: "121" => [1,2,1], [12,1], [1,21]
Length 4: "1212" => [1,2,1,2], [1,21,2], [12,1,2], [1,2,12], [12,12]
...
Let's look closer at length 3 and 4.

Length 3: "121" => [1,2,1], [12,1], [1,21]
We can decompose the three combinations into two parts:

Append self
That is, append "1" to all the combinations in len 2:
[1,2] [12] + [1] => [1,2,1], [12,1]
Append self and the previous digit, if valid (10 to 26)
That is, append "21" to all the combinations in len 1:
[1] + [21] => [1,21]
Length 4: "1212" => [1,2,1,2], [1,21,2], [12,1,2], [1,2,12], [12,12]
We can again decompose the five combinations into two parts:

Append self
That is, append "2" to all the combinations in len 3:
[1,2,1], [12,1], [1,21] + [2] => [1,2,1,2], [1,21,2], [12,1,2]
Append self and the previous digit, if valid (10 to 26)
That is, append "12" to all the combinations in len 2:
[1,2], [12] + [12] => [1,2,12], [12,12]
Therefore, we can generlize the logic into the following:

f(i) = f(i-1) if we found valid one-digit num, i.e. 1 to 9 (0 is an edge case)
f(i) += f(i-2) if we found valid two-digit num, i.e. 10 to 26
Similar as in fibonacci problem, we just need a constant space dp to store the previous two states.

https://leetcode.com/problems/decode-ways/discuss/650945/Python-DP-O(1)-space-clear-explanation
"""

def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, len(s)):
            temp = 0
            if 1 <= int(s[i]) <= 9:
                temp = dp[1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += dp[0]
            dp = [dp[1], temp]
        return dp[1]
