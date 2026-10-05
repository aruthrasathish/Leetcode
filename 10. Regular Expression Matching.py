class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern finished
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # If next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                result = (
                    dp(i, j + 2) or
                    (first_match and dp(i + 1, j))
                )
            else:
                result = first_match and dp(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dp(0, 0)
