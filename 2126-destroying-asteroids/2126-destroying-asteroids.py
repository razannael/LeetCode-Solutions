import numpy as np
from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # 1. Optimal ordering — sort ascending (greedy choice)
        H = np.sort(np.array(asteroids, dtype=np.int64))

        # 2. Planet mass vector at each collision step
        # cumulative[i] = planet mass BEFORE absorbing H[i]
        cumulative = mass + np.cumsum(H) - H

        # 3. Vectorized projection: H(final) = P @ H where P[i,i] = 1 iff absorbed
        # Planet survives all collisions iff cumulative >= H at every step
        return bool(np.all(cumulative >= H))        