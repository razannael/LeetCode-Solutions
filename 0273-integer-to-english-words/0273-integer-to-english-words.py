class Solution:
    chart = [
        (1000_000_000_000_000, "Quadrillion"), (1_000_000_000_000, "Trillion"),
        (1_000_000_000, "Billion"), (1_000_000, "Million"), (1_000, "Thousand"),
        (100, "Hundred"), (90, "Ninety"), (80, "Eighty"), (70, "Seventy"),
        (60, "Sixty"), (50, "Fifty"), (40, "Forty"), (30, "Thirty"), (20, "Twenty"),
        (19, "Nineteen"), (18, "Eighteen"), (17, "Seventeen"), (16, "Sixteen"),
        (15, "Fifteen"), (14, "Fourteen"), (13, "Thirteen"), (12, "Twelve"),
        (11, "Eleven"), (10, "Ten"), (9, "Nine"), (8, "Eight"), (7, "Seven"),
        (6, "Six"), (5, "Five"), (4, "Four"), (3, "Three"), (2, "Two"), (1, "One"),
    ]

    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        ans = []
        for n, word in self.chart:   
            div = num // n
            if div:
                if n >= 100:
                    ans.append(self.numberToWords(div))
                ans.append(word)
                num %= n
        return " ".join(ans)