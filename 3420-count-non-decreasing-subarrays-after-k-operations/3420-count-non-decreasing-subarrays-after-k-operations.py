class Solution:
    def countNonDecreasingSubarrays(self, A: List[int], k: int) -> int:
        A = A[::-1]
        res = 0
        q = deque()
        i = 0
        for j in range(len(A)):
            while q and A[q[-1]] < A[j]:
                r = q.pop()
                l = q[-1] if q else i - 1
                k -= (r - l) * (A[j] - A[r])
            q.append(j)
            while k < 0:
                k += A[q[0]] - A[i]
                if q[0] == i:
                    q.popleft()
                i += 1
            res += j - i + 1
        return res
        