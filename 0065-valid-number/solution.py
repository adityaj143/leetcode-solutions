class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        if not s:
            return False

        if 'e' in s or 'E' in s:
            parts = s.replace('E', 'e').split('e')

            if len(parts) != 2:
                return False

            base, exponent = parts

            if not self.isInteger(exponent):
                return False
        else:
            base = s

        return self.isDecimal(base)

    def isInteger(self, s: str) -> bool:
        if not s:
            return False

        if s[0] in '+-':
            s = s[1:]

        return s.isdigit()

    def isDecimal(self, s: str) -> bool:
        if not s:
            return False

        if s[0] in '+-':
            s = s[1:]

        if not s:
            return False

        parts = s.split('.')

        if len(parts) > 2:
            return False

        if len(parts) == 1:
            return parts[0].isdigit()

        left, right = parts

        return (left.isdigit() and right.isdigit()) or \
               (left.isdigit() and right == '') or \
               (left == '' and right.isdigit())
