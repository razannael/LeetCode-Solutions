class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def get_count(prefix, n):
            count = 0
            current = prefix
            next_prefix = prefix + 1
            while current <= n:
                count += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return count

        curr = 1
        k -= 1  # starting from 1

        while k > 0:
            count = get_count(curr, n)
            if count <= k:
                curr += 1
                k -= count
            else:
                curr *= 10
                k -= 1

        return curr