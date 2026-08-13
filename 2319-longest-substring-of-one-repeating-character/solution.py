class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        size = 4 * self.n

        self.left_char = [''] * size
        self.right_char = [''] * size
        self.prefix = [0] * size
        self.suffix = [0] * size
        self.best = [0] * size
        self.length = [0] * size

        self.build(1, 0, self.n - 1, s)

    def build(self, node, l, r, s):
        if l == r:
            self.left_char[node] = s[l]
            self.right_char[node] = s[l]
            self.prefix[node] = 1
            self.suffix[node] = 1
            self.best[node] = 1
            self.length[node] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid, s)
        self.build(node * 2 + 1, mid + 1, r, s)

        self.merge(node)

    def merge(self, node):
        left = node * 2
        right = node * 2 + 1

        self.length[node] = self.length[left] + self.length[right]

        self.left_char[node] = self.left_char[left]
        self.right_char[node] = self.right_char[right]

        self.prefix[node] = self.prefix[left]
        self.suffix[node] = self.suffix[right]

        self.best[node] = max(self.best[left], self.best[right])

        # The two segments can be joined
        if self.right_char[left] == self.left_char[right]:

            self.best[node] = max(
                self.best[node],
                self.suffix[left] + self.prefix[right]
            )

            # Entire left segment has the same character
            if self.prefix[left] == self.length[left]:
                self.prefix[node] = (
                    self.length[left] + self.prefix[right]
                )

            # Entire right segment has the same character
            if self.suffix[right] == self.length[right]:
                self.suffix[node] = (
                    self.length[right] + self.suffix[left]
                )

    def update(self, node, l, r, index, char):
        if l == r:
            self.left_char[node] = char
            self.right_char[node] = char
            self.prefix[node] = 1
            self.suffix[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, char)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, char)

        self.merge(node)

    def change(self, index, char):
        self.update(1, 0, self.n - 1, index, char)

    def get_best(self):
        return self.best[1]


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        tree = SegmentTree(s)

        ans = []

        for char, index in zip(queryCharacters, queryIndices):
            tree.change(index, char)
            ans.append(tree.get_best())

        return ans
