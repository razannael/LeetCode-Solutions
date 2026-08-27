class Solution:
    def lexGreaterPermutation(self, S: str, T: str) -> str:
        S = [ord(c) - 97 for c in S]
        T = [ord(c) - 97 for c in T]
        S.sort(reverse=True)
        ans = []

        for i, x in enumerate(T):
            if x in S:
                S.remove(x)
                if S > T[i+1:]:
                    ans.append(x)
                    continue
                S.append(x)
                S.sort(reverse=True)

            S.sort()
            for y in S:
                if y > x:
                    S.remove(y)
                    ans.append(y)
                    ans.extend(S)
                    break
            break
            
        return "".join(chr(97 + x) for x in ans)