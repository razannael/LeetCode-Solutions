class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 4: return []
        # Generate all the matches
        matches = []
        for i in range(n):
            for j in range(n):
                if i == j: continue
                matches.append([i, j])
        while True:
            shuffled = [m[:] for m in matches]
            random.shuffle(shuffled)
            schedule = []
            for _ in range(len(matches)):
                found = False
                # Greedily find the next valid match
                for i in range(len(shuffled)):
                    a, b = shuffled[i]
                    if not schedule or (a not in schedule[-1] and b not in schedule[-1]):
                        schedule.append(shuffled[i])
                        shuffled.pop(i)
                        found = True
                        break
                # Break if we can't find a valid next match
                if not found:
                    break
            # If we successfully find a valid schedule, leave the loop, else shuffle the matches and try again
            if len(schedule) == len(matches):
                break
        return schedule