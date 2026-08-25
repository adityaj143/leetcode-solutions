class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)

        multiple = k

        while multiple in nums_set:
            multiple += k

        return multiple
