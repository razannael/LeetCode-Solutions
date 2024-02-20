class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        count = 1
        for r in range(1, len(chars) + 1):
            if r < len(chars) and chars[r] == chars[r - 1]:
                count += 1
            else:
                chars[left] = chars[r - 1]
                left += 1
                if count > 1:
                    for s in str(count):
                        chars[left] = s
                        left += 1
                count = 1
        del chars[left:]
        return left
                