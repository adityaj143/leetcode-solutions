from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((v, i) for i, v in enumerate(nums))
        result = [0] * n
        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[i][1] for i in range(start, end + 1))
            values = [arr[i][0] for i in range(start, end + 1)]

            for i, v in zip(indices, values):
                result[i] = v

            start = end + 1

        return result
