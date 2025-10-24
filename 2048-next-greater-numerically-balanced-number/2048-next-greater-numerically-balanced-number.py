class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        nums = []
        self.generate(0, [0] * 10, nums)
        nums.sort()
        for num in nums:
            if num > n:
                return num
        return -1

    def generate(self, num: int, count: list[int], nums: list[int]) -> None:
        if num > 0 and self.is_beautiful(count):
            nums.append(num)
        if num > 1224444:
            return

        for d in range(1, 8):
            if count[d] < d:
                count[d] += 1
                self.generate(num * 10 + d, count, nums)
                count[d] -= 1

    def is_beautiful(self, count: list[int]) -> bool:
        for d in range(1, 8):
            if count[d] != 0 and count[d] != d:
                return False
        return True