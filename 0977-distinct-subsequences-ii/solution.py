class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = 1  
        last = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')

            new_dp = 2 * dp - last[index]
            new_dp %= MOD

            last[index] = dp
            dp = new_dp

        return (dp - 1) % MOD
