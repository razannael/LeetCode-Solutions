class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        dico={i:0 for i in range (1,n+1)}
        logs=sorted(logs,key=lambda x:x[1])
        queries=sorted([query,i] for i,query in enumerate(queries))
        p=len(logs)
        right,left=0,-1
        countNull=n
        res=[0]*len(queries)
        for query,i in queries:
            while right <p and logs[right][1]<=query:
                serv=logs[right][0]
                if dico[serv]==0:
                    countNull-=1
                dico[serv]+=1
                right+=1
            while left+1<p and logs[left+1][1]<query-x:
                left+=1
                serv=logs[left][0]
                dico[serv]-=1
                if dico[serv]==0:
                    countNull+=1
            res[i]=countNull
        return res
            