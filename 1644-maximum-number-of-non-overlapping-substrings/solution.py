class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            idx = ord(ch) - 97
            first[idx] = min(first[idx], i)
            last[idx] = i

        def get_interval(l):
            r = last[ord(s[l]) - 97]
            i = l

            while i <= r:
                idx = ord(s[i]) - 97
                if first[idx] < l:
                    return None
                r = max(r, last[idx])
                i += 1

            return l, r

        intervals = []

        for i in range(n):
            if first[ord(s[i]) - 97] == i:
                interval = get_interval(i)
                if interval:
                    intervals.append(interval)

        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r

        return result
