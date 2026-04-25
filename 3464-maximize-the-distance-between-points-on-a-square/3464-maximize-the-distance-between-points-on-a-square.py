class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:

        def flatten(p: list) -> int:            # flattens points to a 1D array
            x, y = p
            if y == 0   : return x              # bottom
            if x == side: return side + y       # right
            if y == side: return 3 * side  - x  # top
            if x == 0   : return 4 * side  - y  # left

        def notValid(mnDist: int) -> bool:      # finds whether dist fails
            for i, num in enumerate(arr):
                ptr, cnt = i, 1
                
                while cnt < k:
                    j = bisect_left(arr, arr[ptr] + mnDist)
                    if j == len(points): break

                    ptr = j
                    cnt += 1

                    if mnDist + arr[ptr] > num + 4 * side:
                        cnt = 0
                        break

                if cnt == k:
                    return False

            return True

        arr = sorted(map(flatten, points))
        firstFalse = bisect_left(range(0, side + 1), True, key = notValid)
        return firstFalse - 1           # the max min is one less than 
                                        # the min failure