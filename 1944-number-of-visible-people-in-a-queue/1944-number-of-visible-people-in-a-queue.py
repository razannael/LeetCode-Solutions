class Solution:                                                     #                    *
     def canSeePersonsCount(self, heights: List[int]) -> List[int]: #       *            *
                                                    #                       *            *
                                                    #                       *        *   *
                                                    #                       *     *  *   *
                                                    #                       *  *  *  *   *
        ans, stack = [0] * len(heights), deque()    #   Example: heights = [5, 1, 2, 3, 6]
                                                    #      heights[::-1] = [6, 3, 2, 1, 5]
        for i, hgt in enumerate(heights[::-1]):
                                                    #   i    hgt  stack      ans 
            while stack and stack[-1] < hgt:        #  –––   –––  –––––      –––
                ans[i]+= 1                          #   0    10   [6]        [0,0,0,0,0]
                stack.pop()                         #   1     3   [6,3]      [0,1,0,0,0]
                                                    #   2     2   [6,3,2]    [0,1,1,0,0]  
            if stack: ans[i]+= 1                    #   3     1   [6,3,2,1]  [0,1,1,1,0]
                                                    #   4     5   [6,5]      [0,1,1,1,4]
            stack.append(hgt)
                                                    #    ans[::-1] = [4,1,1,1,0]  <-- return
        return ans[::-1]