from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]

            pick_left = nums[i] - dp(i + 1, j)
            pick_right = nums[j] - dp(i, j - 1)

            return max(pick_left, pick_right)

        return dp(0, len(nums) - 1) >= 0
