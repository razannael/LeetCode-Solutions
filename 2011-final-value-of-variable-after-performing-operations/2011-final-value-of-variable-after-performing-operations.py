class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op_dict = {"--X" : -1, "X--" : -1,
                 "++X" : 1, "X++" : 1}
        return sum(op_dict[op] for op in operations)