class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i, (x1, y1) in enumerate(points):
            y = -inf
            for (x2, y2) in points[i + 1:]:
                if y1 >= y2 > y:
                    res += 1
                    y = y2
        return res     