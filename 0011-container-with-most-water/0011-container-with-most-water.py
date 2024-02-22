class Solution:
    def maxArea(self, height: List[int]) -> int:
      i = 0
      j = len(height) - 1
      maxArea = -inf
      currMax = -inf
      while i < j :
          currMax = min(height[i], height[j]) * (j-i)
          maxArea = max(currMax, maxArea)
          if height[i]< height[j]:
              currentIndex = i
              while i < j and height[currentIndex] >= height[i]:
                  i+=1
          else:
              currentIndex = j
              while i < j and height[currentIndex] >= height[j]:
                  j-=1

      return maxArea