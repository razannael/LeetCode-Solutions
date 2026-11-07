class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        n, ans, busy_servers = len(servers), [], []
        free_servers = list(zip(servers, range(n)))
        heapify(free_servers)

        for time, task in enumerate(tasks):
            
            while busy_servers:
                sec, wgt, idx = busy_servers[0]
                if sec != time: break

                heappush(free_servers, (wgt, idx))
                heappop(busy_servers)

            if free_servers == []:
                sec, wgt, idx = heappop(busy_servers)
                heappush(busy_servers, (sec + task, wgt, idx))

            else:
                wgt, idx = heappop(free_servers)
                heappush(busy_servers, (time + task, wgt, idx))
                
            ans.append(idx)

        return ans