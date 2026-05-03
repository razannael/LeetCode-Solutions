class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1. Cardinality Invariance (The first principle of Isomorphism)
        if len(s) != len(goal):
            return False
            
        # 2. The Orbit Check
        # Mapping s onto its cyclic manifold (s + s) covers all possible 
        # states in the cyclic group of order n.
        return goal in (s + s)        