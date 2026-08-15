class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        
        xor = 0
        for x in nums:
            xor ^= x
        
        if xor != 0:
            return n
        
     
        for x in nums:
            if x != 0:
                return n - 1
   
        return 0
