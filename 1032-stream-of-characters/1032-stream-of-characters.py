class StreamChecker:
    class Node:
        __slots__ = ("children", "end")
        def __init__(self):
            self.children = {}  # char -> Node
            self.end = False

    def __init__(self, words):
        self.root = self.Node()
        self.max_len = 0

        for w in words:
            self.max_len = max(self.max_len, len(w))
            node = self.root
            for ch in reversed(w):
                if ch not in node.children:
                    node.children[ch] = self.Node()
                node = node.children[ch]
            node.end = True

        self.stream = []  

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        if len(self.stream) > self.max_len:
            self.stream.pop(0)

        node = self.root
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.end:
                return True
        return False