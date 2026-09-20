class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s, 1):
            reverse_pos = 26 - (ord(ch) - ord('a'))
            ans += reverse_pos * i

        return ans
