class Fancy:
    def __init__(self):
        self.sequence = []  # To store the actual values
        self.add = 0  # Increment to add to each value
        self.mul = 1  # Multiplier for each value

    def append(self, val: int) -> None:
        # Adjust the new value with current add and mul
        adjusted_value = (val - self.add) * pow(self.mul, -1, 10**9 + 7) % (10**9 + 7)
        self.sequence.append(adjusted_value)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % (10**9 + 7)

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % (10**9 + 7)
        self.mul = (self.mul * m) % (10**9 + 7)

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        # Return the current value at index idx
        return (self.sequence[idx] * self.mul + self.add) % (10**9 + 7)

