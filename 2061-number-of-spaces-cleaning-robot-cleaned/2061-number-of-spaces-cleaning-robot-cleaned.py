class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:

        rows, cols = len(room), len(room[0])

        # This will contain the cells where the robot got stuck
        # to avoid loop
        stucked_cell = set()

        # The cleaned cells
        cleaned = set()

        # Format: right, down, left, up (MUST BE IN THIS CLOCKWISE FORMAT)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # starting cell
        r, c = 0, 0
        d = 0 # starts by facing right (index in directions array)

        # add the first cell to cleaned
        cleaned.add((r, c))
        # first cell is cleaned
        ans = 1

        # Simulation starts
        while True:

            # If the cell is found in the same direction as before (loop!)
            if (r, c, d) in stucked_cell:
                return ans 
            
            stucked_cell.add((r, c, d))

            dr, dc = directions[d]
            nr, nc = r + dr, c + dc # New direction we're about to go in 

            # Turn right if the robot goes out of bounds or hit an obstacle
            if not (0 <= nr < rows and 0 <= nc < cols) or room[nr][nc] == 1:
                d = (d + 1) % 4 
                continue  # skip

            # if the potential cell is empty and not yet cleaned 
            if room[nr][nc] == 0 and (nr, nc) not in cleaned:
                cleaned.add((nr, nc))

                ans += 1 # cleaned cell count
            
            # Keep moving in the current direction,... 
            # whether the cell was cleaned or not 
            r, c = nr, nc
                