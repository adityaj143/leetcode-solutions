class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Check current character match
            first_match = (
                i < len(s) and 
                (s[i] == p[j] or p[j] == '.')
            )

            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    dp(i, j + 2) or               # Ignore x*
                    (first_match and dp(i + 1, j)) # Use x*
                )
            else:
                result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)
