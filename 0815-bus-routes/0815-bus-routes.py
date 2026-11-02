from collections import defaultdict, deque
from typing import List
class Solution:
    def numBusesToDestination(self,routes: List[List[int]],source:int,target:int)->int:
        if source==target:
            return 0
        stops=defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                stops[stop].append(bus)
        if source not in stops or target not in stops:
            return -1
        q=deque([source])
        visited_buses=set()
        visited_stops={source}
        buses_taken=0
        while q:
            buses_taken+=1
            for i in range(len(q)):
                curr = q.popleft()
                for bus in stops[curr]:
                    if bus in visited_buses:
                        continue
                    visited_buses.add(bus)
                    for nxt in routes[bus]:
                        if nxt==target:
                            return buses_taken
                        if nxt in visited_stops:
                            continue
                        visited_stops.add(nxt)
                        q.append(nxt)
        return -1    