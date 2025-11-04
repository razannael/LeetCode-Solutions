class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # count number of ones
        ones = sum(arr)
        if ones % 3 != 0:
            return [-1, -1]
        elif ones == 0:  # special case: all zeros
            return [0, 2]
        
        # find the start index of each group of ones
        c = 0
        starts = []
        for i, d in enumerate(arr):
            if d == 1:
                if c % (ones // 3) == 0:
                    starts.append(i)
                c += 1

        # scan the groups in parallel to compare digits
        i, j, k = starts
        while k < len(arr):  # note that the last/rightmost group must include all digits till the end
            if arr[i] == arr[j] == arr[k]:
                i += 1
                j += 1
                k += 1
            else:
                return [-1, -1]
        return [i-1, j]