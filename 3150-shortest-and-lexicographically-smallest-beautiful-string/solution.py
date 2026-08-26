class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):
            curr = s[ones[i]:ones[i + k - 1] + 1]

            if not ans or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans):
                ans = curr

        return ans
