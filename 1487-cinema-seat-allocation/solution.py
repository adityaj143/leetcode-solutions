class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

  

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        
        ans = (n - len(rows)) * 2

        
        for seats in rows.values():
            left = all(seat not in seats for seat in range(2, 6))   
            middle = all(seat not in seats for seat in range(4, 8)) 
            right = all(seat not in seats for seat in range(6, 10)) 

            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1

        return ans
