class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totalTime = 0

        for i in range(1, len(points)):

            previousPoint = points[i - 1]
            currentPoint = points[i]

            xDistance = abs(currentPoint[0] - previousPoint[0])
            yDistance = abs(currentPoint[1] - previousPoint[1])

            totalTime += max(xDistance, yDistance)

        return totalTime

        