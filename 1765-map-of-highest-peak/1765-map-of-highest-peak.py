class Solution:
    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        m, n = len(is_water), len(is_water[0])
        res = [[0 for j in range(n)] for i in range(m)]

        def get_water_cells():
            return [(i, j) for i in range(m) for j in range(n) if is_water[i][j] == 1]
        
        def get_neighbors(cells, seen):
            nonlocal m, n
            res = []
            for (i, j) in cells:
                for x in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if (0 <= x[0] < m) and (0 <= x[1] < n) and x not in seen:
                        seen.add(x)
                        res.append(x)
            return res

        water_cells = get_water_cells()
        seen = set(water_cells)
        cur_cells = get_neighbors(water_cells, seen)
        cur_val = 1
        while len(cur_cells) > 0:
            for cell in cur_cells:
                res[cell[0]][cell[1]] = cur_val
            cur_cells = get_neighbors(cur_cells, seen)
            cur_val += 1
        return res