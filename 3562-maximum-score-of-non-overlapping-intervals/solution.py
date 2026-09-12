from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in arr]

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        dp_score = [[0] * (n + 1) for _ in range(5)]
        dp_indices = [[()] * (n + 1) for _ in range(5)]

        for k in range(1, 5):
            for i in range(n - 1, -1, -1):
                skip_score = dp_score[k][i + 1]
                skip_indices = dp_indices[k][i + 1]
                l, r, w, idx = arr[i]
                take_score = w + dp_score[k - 1][nxt[i]]

                take_indices = tuple(
                    sorted((idx,) + dp_indices[k - 1][nxt[i]])
                )

                if take_score > skip_score:
                    dp_score[k][i] = take_score
                    dp_indices[k][i] = take_indices
                elif take_score < skip_score:
                    dp_score[k][i] = skip_score
                    dp_indices[k][i] = skip_indices
                else:
                    if take_indices < skip_indices:
                        dp_score[k][i] = take_score
                        dp_indices[k][i] = take_indices
                    else:
                        dp_score[k][i] = skip_score
                        dp_indices[k][i] = skip_indices

        return list(dp_indices[4][0])

