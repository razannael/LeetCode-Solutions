import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # sort by: 1) start time, and if tie: 2) end time
        events = sorted(events, key= lambda x:(x[0], x[1]))
        current_day = 0
        heap = []
        count = 0
        i =0
        while i < len(events) or heap:
            #if heap is empty
            if not heap:
                current_day = events[i][0]
            while i < len(events) and events[i][0] <= current_day:
                heapq.heappush(heap, events[i][1])
                i+=1
            
            heapq.heappop(heap)
            count += 1
            current_day += 1

            while heap and heap[0] < current_day:
                heapq.heappop(heap)
        
        return count