class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x, y = 1, 1000
        while x <= 1000 and 1 <= y: 
            if customfunction.f(x, y) < z: x += 1
            elif customfunction.f(x, y) > z: y -= 1
            else:
                ans.append([x, y])
                x += 1
                y -= 1
        return ans 