class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        diff = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                diff += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                diff -= int(num[i])

        q_diff = left_q - right_q

        # Odd difference in '?' counts => Alice can force a win
        if q_diff % 2 != 0:
            return True

        # Bob wins only if the existing difference can be exactly balanced
        return diff + 9 * q_diff // 2 != 0
