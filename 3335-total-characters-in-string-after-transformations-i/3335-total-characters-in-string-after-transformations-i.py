class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        return sum(reduce(lambda q,_:(q[-1],q[0]+q[-1])+q[1:-1], range(t),
            itemgetter(*ascii_lowercase)(Counter(s))))%(10**9+7)