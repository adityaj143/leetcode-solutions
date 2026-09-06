class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1

        for ch in s:
            for j in range(len(t), 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]
