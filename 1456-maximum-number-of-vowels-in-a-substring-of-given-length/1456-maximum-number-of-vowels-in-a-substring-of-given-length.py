class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_v = 0
        curr_v =0
        for i in range(len(s)):
            if s[i] in vowels:
              curr_v += 1
            if i >= k:
                if s[i - k] in vowels:
                    curr_v -= 1
            max_v = max(max_v, curr_v)

        return max_v
