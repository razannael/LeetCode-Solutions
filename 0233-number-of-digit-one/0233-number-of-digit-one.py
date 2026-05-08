class Solution:
    def countDigitOne(self, n: int) -> int:
        def count(add,n_digit):
            c = 0
            for d in range(0,n_digit+1):
                c += (d+add)*math.comb(n_digit,d)*9**(n_digit-d)
            return c
        res = 0
        n_list = [int(x) for x in str(n)]
        count_1 = 0
        for i in range(len(n_list)-1):
            if n_list[i] == 1:
                res += count(count_1,len(n_list)-i-1)
                count_1 += 1
            elif n_list[i] > 1:
                leading = n_list[i]-1
                res += count(count_1,len(n_list)-i-1)*leading+count(count_1+1,len(n_list)-i-1)
        res += count_1*(n_list[-1]+1)
        if n_list[-1] >= 1:
            res += 1
        return res