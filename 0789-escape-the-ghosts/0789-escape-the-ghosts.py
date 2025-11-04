import math
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def distance(i,j,x,y):
            return abs(i-x)+abs(j-y)
        thresh=distance(0,0,target[0],target[1])
        # print(thresh)
        for i in ghosts:
            # print(distance(i[0],i[1],target[0],target[1]))
            if distance(i[0],i[1],target[0],target[1])<=thresh:
                return False
        return True