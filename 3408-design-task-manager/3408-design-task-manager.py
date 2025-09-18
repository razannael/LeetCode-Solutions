class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.map = {}
        self.heap = []
        for u,t,p in tasks:
            heappush(self.heap,(-p,-t))
            self.map[t]=(u,p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.map[taskId]=(userId,priority)
        heappush(self.heap,(-priority,-taskId))
        # print("after add:",self.map)

    def edit(self, taskId: int, newPriority: int) -> None:
        heappush(self.heap,(-newPriority,-taskId))
        u,_=self.map[taskId]
        self.map[taskId]=(u,newPriority)
        # print("after edit:",self.map)

    def rmv(self, taskId: int) -> None:
        # print(self.map)
        del self.map[taskId]

    def execTop(self) -> int:
        # print("exec:",self.map,self.heap)
        while self.heap:
            p,t=heappop(self.heap)
            t=-t
            p=-p
            if t not in self.map or self.map[t][1]!=p:
                continue
            u,_ = self.map[t]
            del self.map[t]
            return u
        return -1