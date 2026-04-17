class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        for _ in range(volume):
            min_left = min_right = heights[k]
            idx = k

            # Scan left
            for i in range(k, -1, -1):
                if heights[i] < min_left:
                    idx = i
                    min_left = heights[i]
                elif heights[i] > min_left:
                    break
            
            if idx != k:
                heights[idx] += 1
                continue 

            # Scan right
            for i in range(k, len(heights)):
                if heights[i] < min_right:
                    idx = i
                    min_right = heights[i]
                elif heights[i] > min_right:
                    break

            heights[idx] += 1
        return heights