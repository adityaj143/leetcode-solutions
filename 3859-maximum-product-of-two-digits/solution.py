class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second = 0

        while n > 0:
            digit = n % 10

            if digit >= largest:
                second = largest
                largest = digit
            elif digit > second:
                second = digit

            n //= 10

        return largest * second
