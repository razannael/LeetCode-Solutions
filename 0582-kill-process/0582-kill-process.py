from collections import defaultdict
from collections import deque

class Solution:

    def killProcess(self, pid: List[int], parent_ids: List[int], kill: int) -> List[int]:
        lookup = defaultdict(list)    # store hashmap of parent -> children
        for cid, parid in zip(pid, parent_ids):
            lookup[parid].append(cid)
        dq = deque([kill])
        res = []
        while dq:
            node = dq.popleft()
            if node in lookup:
                dq.extend(lookup[node])
            res.append(node)

        return res