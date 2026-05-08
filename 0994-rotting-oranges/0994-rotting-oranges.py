class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])
        grid_copy = deepcopy(grid)#madde a copy of the main so will chnge it now
        fresh = 0 
        que = deque()
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] ==1:
                    fresh+=1
                if grid_copy[r][c] ==2:
                    que.append((r,c))
                    # rotten hai to add to que if 1 mtlb fresh hai toh +=1
        time= 0 
        while que and fresh>0:
            time+=1
            totalrotten = len(que)
            for k in range(totalrotten):#jitne rotten unke liye loop itr kro 
                x,y = que.popleft()
                dirs = [(-1,0),(0,1),(1,0),(0,-1)]
                for dx,dy in dirs :
                    xx = x+dx
                    yy = y+dy
                    if xx>=rows or yy >=cols or xx <0 or yy<0:
                        continue
                    if grid_copy[xx][yy] != 1 :#fresh ka alawa kuch bhi ho chalte rahe 
                        continue
                    fresh-=1
                    grid_copy[xx][yy] = 2#mark it rotten as we reduce one fresh so balaances
                    que.append((xx , yy))
        return time if fresh==0 else -1