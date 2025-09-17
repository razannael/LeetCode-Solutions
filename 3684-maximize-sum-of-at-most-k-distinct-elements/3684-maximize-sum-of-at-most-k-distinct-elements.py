    def maxKDistinct(self, A: List[int], k: int) -> List[int]:
        return nlargest(k, set(A))