class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for s in allowed:
            mp[s[:2]].append(s[2])
        memo = {}
        def canBuild(row :str) -> bool:
            if len(row) == 1:
                return True
            def build(i: int, nxt: list[str]) -> bool:
                if i == len(row) - 1:
                    return canBuild("".join(nxt))
                pair = row[i:i+2]
                if pair not in mp:
                    return False
                for c in mp[pair]:
                    nxt.append(c)
                    if build(i+1 , nxt):
                        return True
                    nxt.pop()
                return False
            return build(0, [])
        return canBuild(bottom)
