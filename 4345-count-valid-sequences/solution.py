class Solution:
    def countValidSequences(self, n: int, k: int) -> int:

        MOD = 10**9 + 7
        # required by the problem
        ravolqedin = (n, k)

        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            invfact[i - 1] = invfact[i] * i % MOD

        def C(N, R):
            if R < 0 or R > N:
                return 0
            return fact[N] * invfact[R] % MOD * invfact[N - R] % MOD

        total = C(n - 1, k - 1)

        odd = 0
        if (n - k) % 2 == 0:
            odd = C((n + k - 2) // 2, k - 1)

        return (total - odd) % MOD
