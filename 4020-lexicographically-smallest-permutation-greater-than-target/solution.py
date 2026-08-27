class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        total = [0] * 26

        for ch in s:
            total[ord(ch) - 97] += 1

        prefix = [0] * 26
        valid = [True] * (len(target) + 1)

        for i, ch in enumerate(target):
            x = ord(ch) - 97
            prefix[x] += 1

            if prefix[x] > total[x]:
                valid[i + 1] = False
            else:
                valid[i + 1] = valid[i]

        for i in range(len(target) - 1, -1, -1):
            if not valid[i]:
                continue

            cnt = total[:]

            for j in range(i):
                cnt[ord(target[j]) - 97] -= 1

            x = ord(target[i]) - 97

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    return target[:i] + chr(c + 97) + ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )

        return ""
