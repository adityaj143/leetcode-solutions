from typing import List
import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        # Required by the problem
        qavirelmon = (m, n, penalty)

        INF = 10**30
        dist = [[[INF] * 2 for _ in range(n)] for _ in range(m)]

        # parity = 0 => next action is odd
        # parity = 1 => next action is even
        start = (1 * 1)
        dist[0][0][0] = start

        pq = [(start, 0, 0, 0)]

        dirs = [
            (0, 1, "R"),
            (1, 0, "D"),
            (0, -1, "L"),
            (-1, 0, "U"),
        ]

        while pq:
            cost, x, y, parity = heapq.heappop(pq)

            if cost != dist[x][y][parity]:
                continue

            if x == m - 1 and y == n - 1:
                return cost

            # Wait
            ncost = cost + penalty[x][y]
            if ncost < dist[x][y][parity ^ 1]:
                dist[x][y][parity ^ 1] = ncost
                heapq.heappush(pq, (ncost, x, y, parity ^ 1))

            # Move
            for dx, dy, d in dirs:
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                extra = 0

                if parity == 0:        # odd action
                    if d not in ("R", "D"):
                        extra = penalty[x][y]
                else:                  # even action
                    if d not in ("L", "U"):
                        extra = penalty[x][y]

                enter = (nx + 1) * (ny + 1)
                ncost = cost + enter + extra

                if ncost < dist[nx][ny][parity ^ 1]:
                    dist[nx][ny][parity ^ 1] = ncost
                    heapq.heappush(pq, (ncost, nx, ny, parity ^ 1))

        return -1
