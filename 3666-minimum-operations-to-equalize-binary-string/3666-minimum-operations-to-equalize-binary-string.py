class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')  # initial zeros

        if z0 == 0:
            return 0  # already all ones

        # sets of unvisited states (sorted lists)
        even = list(range(0, n + 1, 2))
        odd = list(range(1, n + 1, 2))
        visited = [False] * (n + 1)

        def erase_range(lst, L, R):
            """Erase all numbers in [L, R] from sorted list and return them."""
            l = bisect_left(lst, L)
            r = bisect_right(lst, R)
            result = lst[l:r]
            del lst[l:r]
            return result

        q = deque([(z0, 0)])
        visited[z0] = True

        while q:
            z, dist = q.popleft()
            i_min = max(0, k - (n - z))
            i_max = min(k, z)
            L = z + k - 2 * i_max
            R = z + k - 2 * i_min
            p = (z + k) % 2

            if p == 0:
                next_states = erase_range(even, max(0, L), min(n, R))
            else:
                next_states = erase_range(odd, max(0, L), min(n, R))

            for z2 in next_states:
                if not visited[z2]:
                    if z2 == 0:
                        return dist + 1
                    visited[z2] = True
                    q.append((z2, dist + 1))

        return -1