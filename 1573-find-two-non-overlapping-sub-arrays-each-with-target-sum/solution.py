from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * (n + 1)
        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                if best[left] != float('inf'):
                    ans = min(ans, length + best[left])

                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]

        return -1 if ans == float('inf') else ans
