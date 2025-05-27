class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        integer_part = numerator // denominator
        result = "-" if negative else ""
        result += str(integer_part) + "."

        remainder = numerator % denominator
        remainders = {}
        decimal_part = []

        while remainder != 0:
            if remainder in remainders:
                repeat_index = remainders[remainder]
                decimal_part.insert(repeat_index, "(")
                decimal_part.append(")")
                break

            remainders[remainder] = len(decimal_part)
            remainder *= 10
            digit = remainder // denominator
            decimal_part.append(str(digit))
            remainder %= denominator

        return result + "".join(decimal_part)