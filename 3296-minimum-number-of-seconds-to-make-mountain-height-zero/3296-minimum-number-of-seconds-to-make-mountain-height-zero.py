class Solution:
    def minNumberOfSeconds(self, mountainHeight: int,
                workerTimes: List[int], mx = 50_000_500_000) -> int:

        def work_done(days: int)-> int:                             # <- 1)
            work = lambda wt: int(sqrt(8 * days / wt + 1) - 1)//2   # <- 2)
            return sum(map(work,workerTimes))

        poss_days = range( mx * mountainHeight // len(workerTimes))

        return bisect_left(poss_days, 
                               mountainHeight, key = work_done)     # <- 3)