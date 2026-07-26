class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0

        if s > 9 * n:
            return -1

        ans = []

        for _ in range(n):
            digit = min(9, s)
            ans.append(str(digit))
            s -= digit

        return int("".join(ans))
