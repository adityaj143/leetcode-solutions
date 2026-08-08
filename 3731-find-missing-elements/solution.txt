from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(min(nums), max(nums) + 1) if i not in s]