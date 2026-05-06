class Solution:
    def rotateTheBox(self, boxGrid):
        rows, cols = len(boxGrid), len(boxGrid[0])

        for r, row in enumerate(boxGrid):
            new_row = []
            empty = 0

            for i in range(cols - 1, -1, -1):
                if row[i] == '.':
                    empty += 1
                elif row[i] == '#':
                    new_row.append('#')
                else:
                    new_row.extend(['.'] * empty)
                    new_row.append('*')
                    empty = 0

            new_row.extend(['.'] * empty)
            boxGrid[r] = new_row[::-1]

        return [
            [boxGrid[rows - i - 1][j] for i in range(rows)]
            for j in range(cols)
        ]