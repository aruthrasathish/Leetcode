class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Handle overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double the divisor until the next
            # doubling would exceed the dividend
            while (temp << 1) <= dividend:
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the correct sign
        if negative:
            quotient = -quotient

        return quotient
