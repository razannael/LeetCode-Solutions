class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        visited = {0}
        far = 0

        while len(q) > 0:
            i = q.popleft()

            if i == len(s)-1:
                return True

            for j in range(max(far, i+minJump), min(len(s), i+maxJump+1)):
                if s[j] == '0' and j not in visited:
                    q.append(j)
                    visited.add(j)
            far = min(len(s), i+maxJump+1)       
                   
        return False            