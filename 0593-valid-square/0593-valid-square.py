from math import dist

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        a=dist(tuple(p1),tuple(p2))
        b=dist(tuple(p2),tuple(p3))
        c=dist(tuple(p3),tuple(p4))
        d=dist(tuple(p4),tuple(p1))
        e=dist(tuple(p1),tuple(p3))
        f=dist(tuple(p2),tuple(p4))

        if len({a,b,c,d,e,f})==2 and 0 not in {a,b,c,d,e,f}:
            return True
        else:
            return False