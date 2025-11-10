class Solution(object):
    def minOperations(self, nums):
        ans = 0
        seen = [False] * 100001
        mono_stack = [0] * len(nums)  # fixed-size stack
        top = 0

        for curr in nums:
            if curr == 0:
                while top > 0:
                    top -= 1
                    seen[mono_stack[top]] = False
                continue

            while top > 0 and mono_stack[top - 1] > curr:
                top -= 1
                seen[mono_stack[top]] = False

            if not seen[curr]:
                ans += 1
                seen[curr] = True

            mono_stack[top] = curr
            top += 1

        return ans