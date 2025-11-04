class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert(string):
            if '(' in string:
                rep_part = string[string.index('(') + 1:string.index(')')]
                string = string.replace('(', '').replace(')', '')
                string += rep_part * 8

            return string
            
        def round_down(num, decimals):
            return math.floor(float(num) * 10 ** decimals + 0.5) / 10 ** decimals
        
        return round_down(convert(s), 8) == round_down(convert(t), 8)