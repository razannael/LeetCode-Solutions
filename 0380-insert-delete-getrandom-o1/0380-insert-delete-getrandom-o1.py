class RandomizedSet:

    def __init__(self):
        self.nums = {}
        

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums[val]=1
        return True


    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.nums.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()