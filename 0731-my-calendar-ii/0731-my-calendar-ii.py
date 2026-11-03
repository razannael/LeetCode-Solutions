from sortedcontainers import SortedList
class MyCalendarTwo:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start, end):
        self.calendar.add((start,1))
        self.calendar.add((end,-1))

        total = 0 

        for i,j in self.calendar:
            total += j 

            if total == 3:
                self.calendar.remove((start,1))
                self.calendar.remove((end,-1))
                return False 

        return True