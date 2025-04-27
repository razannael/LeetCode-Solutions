class Solution:
    def numberOfArrays(self, diff: List[int], lower: int, upper: int) -> int:
        return (K:=list(accumulate(diff, initial=0))) and max(0, upper-lower+1-max(K)+min(K))
        