class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)

        def dfs(index):
            # Out of bounds or already visited
            if index < 0 or index >= len(arr) or visited[index]:
                return False

            # Found zero
            if arr[index] == 0:
                return True

            visited[index] = True

            # Jump forward or backward
            return dfs(index + arr[index]) or dfs(index - arr[index])

        return dfs(start)