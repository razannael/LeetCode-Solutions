Z = 26


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * Z
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        center = ''
        for i in range(Z):
            if cnt[i] % 2:
                center += chr(i + ord('a'))
            cnt[i] //= 2
        if len(center) > 1:
            return ''
        ans = ''
        for i in range(len(target)):
            if i >= len(target) // 2:
                candidate = target[:i] + center + target[:i][::-1]
                if candidate > target:
                    ans = candidate
                break
            choice = ord(target[i]) - ord('a') + 1
            while choice < Z and cnt[choice] == 0:
                choice += 1
            if choice < Z:
                cur = target[:i] + chr(choice + ord('a'))
                cnt[choice] -= 1
                for j in range(Z):
                    cur += chr(ord('a') + j) * cnt[j]
                ans = cur + center + cur[::-1]
                cnt[choice] += 1
            if cnt[ord(target[i]) - ord('a')]:
                cnt[ord(target[i]) - ord('a')] -= 1
            else:
                break
        return ans