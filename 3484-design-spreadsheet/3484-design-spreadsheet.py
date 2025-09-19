class Spreadsheet:
    def __init__(self, rows: int):
        # Initialize a grid with 26 columns and 'rows' number of rows, all set to 0
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col, row = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self._parse_cell(cell)
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        # Remove the '=' at the start
        formula = formula[1:]
        # Split the formula by '+'
        operands = formula.split('+')
        total = 0
        for operand in operands:
            operand = operand.strip()
            if operand.isdigit():
                # If it's a number, add it directly
                total += int(operand)
            else:
                # Otherwise, it's a cell reference
                col, row = self._parse_cell(operand)
                total += self.grid[row][col]
        return total

    def _parse_cell(self, cell: str) -> tuple:
        # Extract the column letter and row number from the cell reference
        col_letter = cell[0]
        row_number = int(cell[1:])
        # Convert column letter to index (0 for 'A', 1 for 'B', ..., 25 for 'Z')
        col_index = ord(col_letter) - ord('A')
        # Convert 1-indexed row number to 0-indexed row index
        row_index = row_number - 1
        return col_index, row_index
