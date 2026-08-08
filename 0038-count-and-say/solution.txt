class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"

        for _ in range(n - 1):
            temp = ""
            count = 1

            for i in range(1, len(ans)):
                if ans[i] == ans[i - 1]:
                    count += 1
                else:
                    temp += str(count) + ans[i - 1]
                    count = 1

            temp += str(count) + ans[-1]
            ans = temp

        return ans