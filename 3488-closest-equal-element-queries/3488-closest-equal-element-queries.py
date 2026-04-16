class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        indices = defaultdict(list)  # num -> sorted indices
        for i, num in enumerate(nums):
            indices[num].append(i)

        result = []
        for q in queries:
            qind = indices[nums[q]]
            if len(qind) == 1:
                result.append(-1)
            else:
                j = bisect_left(qind, q)
                prev = qind[(j - 1) % len(qind)]
                nextt = qind[(j + 1) % len(qind)]
                result.append(min(
                    (nextt + n - qind[j]) % n,
                    (qind[j] - prev + n) % n,
                ))

        return result