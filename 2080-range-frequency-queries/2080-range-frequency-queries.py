class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.loc = defaultdict(list)
        for i, x in enumerate(arr): self.loc[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.loc: return 0 
        lo = bisect_left(self.loc[value], left)
        hi = bisect_right(self.loc[value], right)
        return hi - lo 