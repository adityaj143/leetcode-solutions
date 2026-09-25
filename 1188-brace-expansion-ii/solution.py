class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def parse(i):
            result = set()
            current = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1
                elif expression[i] == '{':
                    sub, i = parse(i + 1)
                    current = {a + b for a in current for b in sub}
                else:
                    current = {a + expression[i] for a in current}
                    i += 1

            result |= current

            if i < n and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)
        return sorted(result)
