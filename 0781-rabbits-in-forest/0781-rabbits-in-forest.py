class Solution:
    def numRabbits(self, answers):
        answers.sort()
        res = 0
        count = 0

        for i in range(len(answers)):
            if answers[i] == 0:
                res += 1  
            elif i == 0 or answers[i] != answers[i - 1] or count == 0:
                res += answers[i] + 1  
                count = answers[i]
            else:
                count -= 1 
        return res