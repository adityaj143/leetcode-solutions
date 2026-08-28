class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        if n == 1:
            return s if s > target else ""

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        odd_char = ""
        for i in range(26):
            if cnt[i] % 2:
                if odd_char:
                    return ""
                odd_char = chr(ord("a") + i)
            cnt[i] //= 2

        prefix = []

        def check(c):
            left = prefix.copy()
            left.append(c)

            for i in range(25, -1, -1):
                left.extend([chr(ord("a") + i)] * cnt[i])

            palindrome = left + [odd_char] + left[::-1]
            return "".join(palindrome) > target

        for i in range(n // 2):
            found = False

            for j in range(26):
                if cnt[j] == 0:
                    continue

                cnt[j] -= 1

                if check(chr(ord("a") + j)):
                    prefix.append(chr(ord("a") + j))
                    found = True
                    break
                else:
                    cnt[j] += 1

            if not found:
                return ""

            if prefix[i] > target[i]:
                left = prefix[:]

                for j in range(26):
                    left.extend([chr(ord("a") + j)] * cnt[j])

                palindrome = left + [odd_char] + left[::-1]
                return "".join(palindrome)

        ans = prefix + [odd_char] + prefix[::-1]
        return "".join(ans)
