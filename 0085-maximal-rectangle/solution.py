class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for c in range(cols):
                if row[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = [-1]

            for c in range(cols):
                while stack[-1] != -1 and heights[stack[-1]] > heights[c]:
                    h = heights[stack.pop()]
                    width = c - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(c)

            while stack[-1] != -1:
                h = heights[stack.pop()]
                width = cols - stack[-1] - 1
                max_area = max(max_area, h * width)

        return max_area
