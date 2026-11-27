class Solution:
    def trap(self, height):
        n = len(height)
        lmax = []
        rmax = []

        maxx = height[0]
        for i in range(n):
            lmax.append(maxx)
            if height[i] > maxx:
                maxx = height[i]

        maxx = 0
        for i in range(n - 1, -1, -1):
            rmax.append(maxx)
            if height[i] > maxx:
                maxx = height[i]
        rmax = rmax[::-1]

        res = 0
        for i in range(n):
            water = min(lmax[i], rmax[i]) - height[i]
            if water > 0:
                res += water
        return res