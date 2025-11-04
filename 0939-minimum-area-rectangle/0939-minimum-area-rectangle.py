class Solution:
    def minAreaRect(self, points) -> int:
        min_area = inf
        dict_x = defaultdict(set)
        for x, y in points:
            dict_x[x].add(y)
        dict_x = {x: set_y for x, set_y in dict_x.items() if len(set_y) > 1}
        for x1, x2 in combinations(dict_x.keys(), 2):
            for y1, y2 in combinations(dict_x[x1] & dict_x[x2], 2):
                min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
        return min_area if min_area < inf else 0