import numpy as np

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        L = np.array(lcp, dtype=float)

        # Diagonal must equal n - i (suffix length at position i)
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        E = (L > 0).astype(float)

        res = [0] * n
        current_char = 1

        for i in range(n):
            if res[i] > 0: continue
            if current_char > 26: return ""

            v = E[:, i]
            clique_indices = np.where(v > 0.5)[0]

            for idx in clique_indices:
                if res[idx] == 0:
                    res[idx] = current_char
                elif res[idx] != current_char:
                    return ""

            current_char += 1

        word = "".join(chr(ord('a') + c - 1) for c in res)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
                if lcp[i][j] != expected:
                    return ""

        return word