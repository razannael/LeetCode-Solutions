class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        time, max_heap = 0, []
        for duration, last_day in sorted(courses, key=lambda c:c[1]):
            # we can take the course
            if time + duration <= last_day:
                time += duration
                heapq.heappush(max_heap, -duration)
			# we can't take the course. Drop the largest duration course we took before and add 
            # this current shorter course which will fit now due to dropping the other largest one
            elif max_heap and -max_heap[0] > duration and time + duration - (-max_heap[0]) < last_day:
                time += duration - (-heapq.heappop(max_heap))
                heapq.heappush(max_heap, -duration)
        return len(max_heap)