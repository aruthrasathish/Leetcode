class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Numbers ending in 0 cannot be palindromes unless x is 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even number of digits: x == reversed_half
        # Odd number of digits: ignore middle digit using // 10
        return x == reversed_half or x == reversed_half // 10
