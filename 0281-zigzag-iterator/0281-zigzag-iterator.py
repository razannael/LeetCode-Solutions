# class ZigzagIterator:
#     def __init__(self, v1: List[int], v2: List[int]):
#         self.q=deque([iter(v1), iter(v2)])
#         self.nextx=None

#     def next(self) -> int:
#         if self.nextx is not None:
#             to_return=self.nextx
#             self.nextx=None
#             return to_return
#         if self.hasNext():
#             return self.nextx
#         raise StopIteration()
        

#     def hasNext(self) -> bool:
#         if self.nextx is not None:
#             return True
#         while self.q:
#             cur=self.q.popleft()
#             try:
#                 self.nextx=next(cur)
#                 self.q.append(cur)
#                 return True
#             except StopIteration as e:
#                continue
#         return False
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.q = deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.q)
# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())