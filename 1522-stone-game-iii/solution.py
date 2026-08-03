class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            curr = 0

            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i + k]
                    best = max(best, curr - dp[i + k + 1])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
