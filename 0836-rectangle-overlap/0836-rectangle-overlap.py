class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])

        if left < right and bottom < top:
            return True     
        return False