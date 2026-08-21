class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])

                        if cur_lcm > x:
                            break
                else:
                    amount = x // cur_lcm

                    if bits % 2:
                        total += amount
                    else:
                        total -= amount

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
