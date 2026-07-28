from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        first_half = []
        middle = ""

        for ch in sorted(freq.keys()):
            first_half.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        first = "".join(first_half)
        return first + middle + first[::-1]
