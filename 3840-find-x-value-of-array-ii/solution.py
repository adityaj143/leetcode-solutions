from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        prod = [1] * (4 * n)
        pref = [[0] * k for _ in range(4 * n)]

        def merge(node):
            left = node * 2
            right = left + 1
            lp = prod[left]
            prod[node] = (lp * prod[right]) % k

            for x in range(k):
                pref[node][x] = pref[left][x]

            for x in range(k):
                pref[node][(lp * x) % k] += pref[right][x]

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                prod[node] = v
                pref[node][v] = 1
                return

            m = (l + r) // 2
            build(node * 2, l, m)
            build(node * 2 + 1, m + 1, r)
            merge(node)

        def update(node, l, r, idx, value):
            if l == r:
                v = value % k
                prod[node] = v
                pref[node] = [0] * k
                pref[node][v] = 1
                return

            m = (l + r) // 2

            if idx <= m:
                update(node * 2, l, m, idx, value)
            else:
                update(node * 2 + 1, m + 1, r, idx, value)

            merge(node)

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return prod[node], pref[node][:]

            m = (l + r) // 2

            if qr <= m:
                return query(node * 2, l, m, ql, qr)

            if ql > m:
                return query(node * 2 + 1, m + 1, r, ql, qr)

            lp, lcnt = query(node * 2, l, m, ql, qr)
            rp, rcnt = query(node * 2 + 1, m + 1, r, ql, qr)

            cnt = lcnt[:]

            for x in range(k):
                cnt[(lp * x) % k] += rcnt[x]

            return (lp * rp) % k, cnt

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            _, cnt = query(1, 0, n - 1, start, n - 1)
            ans.append(cnt[x])

        return ans
