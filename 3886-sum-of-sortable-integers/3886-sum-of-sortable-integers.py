class Solution:
    def operation(self, k, nums):
        n = len(nums)
        chunks = n // k
        minMax = []

        for i in range(chunks):
            start = i * k
            mini = float('inf')
            maxi = float('-inf')
            cnt = 0

            for j in range(k):
                curr = nums[start + j]
                next_val = nums[start + (j + 1) % k]

                mini = min(mini, curr)
                maxi = max(maxi, curr)

                if curr > next_val:
                    cnt += 1

            if cnt > 1:
                return False

            minMax.append((mini, maxi))

        for i in range(chunks - 1):
            if minMax[i][1] > minMax[i + 1][0]:
                return False

        return True

    def sortableIntegers(self, nums):
        n = len(nums)
        ans = 0

        i = 1
        while i * i <= n:
            if n % i == 0:
                if self.operation(i, nums):
                    ans += i

                if i != n // i:
                    if self.operation(n // i, nums):
                        ans += (n // i)
            i += 1

        return ans