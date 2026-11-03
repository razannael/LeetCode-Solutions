class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:

        ans, d, cnt = [], defaultdict(int), 0

        for i, color in queries:

            if d[i]: cnt-= (d[i-1] == d[i])+(d[i+1] == d[i])
            d[i] = color
            if d[i]: cnt+= (d[i-1] == d[i])+(d[i+1] == d[i])

            ans.append(cnt)

        return ans