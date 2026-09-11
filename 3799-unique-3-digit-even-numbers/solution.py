from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            
            required = [a, b, c]
            available = digits.copy()

            possible = True

            for digit in required:
                if digit in available:
                    available.remove(digit)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count
