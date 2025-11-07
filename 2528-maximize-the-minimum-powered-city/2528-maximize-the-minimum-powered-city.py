class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        lo = min(stations)
        hi = max(stations) * len(stations) + k
        
        # Adding bunch of (r+1) 0s to left, and (r) 0s to right for handling corner cases.
        stations = [0]*(r) + stations + [0]*r
        res = lo
        
        def check(med):
            available = k
            ind = r                         # ind of our first city
            
            window = sum(stations[:2*r])    # Sliding window will store power of stations for city
                                            # initially it will have values from 0th station to (r-1) stn
            
			# This will store, in which city we have added station because of deficiency. 
			# Because we need to remove that val when that city is out of range.
            added = defaultdict(int)        
                                            
            while ind < len(stations)-r:
                window += stations[ind + r]
                
                if window < med:
                    diff = med-window
                    if diff>available:
                        return False
                    window+=diff
                    added[ind+r]=diff 
                    available-=diff
					
                window -= (stations[ind - r] + added[ind-r])
                ind+=1
            return True
        
        while lo<=hi:                       # Typical Binary Search
            m = (lo + hi )//2
            if check(m):
                res = m
                lo = m + 1
            else:
                hi = m-1
        return res