class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        # Clockwise directions (x, y): left, up, right, down
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Keep track of visited cells
        visited = set()

        # Turn 180, move, Turn 180 to go back to the previous cell
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        # DFS Params: x, y, direction
        def robo_dfs(x, y, direction):
            visited.add((x, y))
            robot.clean()

            for i in range(4):
                new_direction = (direction + i) % 4

                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]

                # Check for valid move
                if (new_x, new_y) not in visited and robot.move():
                    # Try moving in next direction
                    robo_dfs(new_x, new_y, new_direction)
                    # Backtrack: call go_back()
                    go_back()

                # turn robot 90 degrees to make sure robot is aligned
                robot.turnRight()

        robo_dfs(0, 0, 0)