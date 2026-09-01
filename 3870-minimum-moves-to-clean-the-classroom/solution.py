from typing import List
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        target = (1 << k) - 1
        best = [[-1] * (1 << k) for _ in range(m * n)]
        q = deque([(sr, sc, 0, energy, 0)])
        best[sr * n + sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, moves = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                if classroom[nr][nc] == 'X' or e == 0:
                    continue

                ne = e - 1
                nmask = mask

                if (nr, nc) in litter:
                    nmask |= 1 << litter[(nr, nc)]

                if classroom[nr][nc] == 'R':
                    ne = energy

                if nmask == target:
                    return moves + 1

                idx = nr * n + nc

                if ne > best[idx][nmask]:
                    best[idx][nmask] = ne
                    q.append((nr, nc, nmask, ne, moves + 1))

        return -1
