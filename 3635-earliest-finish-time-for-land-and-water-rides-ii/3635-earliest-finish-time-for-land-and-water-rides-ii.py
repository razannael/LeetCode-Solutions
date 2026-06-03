#LC 3635, 3633 Earliest Finish Time for Land and Water Rides 
class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        minLandEnd=min(s+d for s, d in zip(ls, ld))
        minWaterEnd=min(s+d for s,d in zip(ws, wd))
        lw=min(max(minLandEnd, s)+d for s, d in zip(ws, wd))
        wl=min(max(minWaterEnd, s)+d for s,d in zip(ls, ld))
        return min(lw, wl)
        